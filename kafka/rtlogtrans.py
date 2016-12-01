# encoding=utf-8
'''
这个脚本的目的：
1.根据配置文件实时读取源日志文件内容写入到kafka中，并实现了配置文件reload功能。
2.在多模块日志需要读取的情况下，启动多进程读取。实现一个模块日志对应一组进程的方式。
3.能够将读取进度持久化到文件中，为出现故障时补日志提供依据
4.能够根据持久化文件进行补日志操作。

实时日志运行方式：env/bin/python rtlogtrans.py
补日志运行方式：
    补单个文件日志的方式
    env/bin/python rtlogtrans.py 模块名  要补日志的源日志文件绝对路径
    补多个文件日志的方式（只要给出开始文件名  结束文件名即可，中间文件程序会自动算出）
    env/bin/python rtlogtrans.py 模块名  要补日志的源日志文件绝对路径（开始文件） 要补日志的源日志文件绝对路径（结束文件）

日志文件约束：
1. 日志实时写入的文件的文件名固定，比如叫api.m.mtime.cn_access.log  不可以为api.m.mtime.cn_2016072817.log
2. 往期日志文件必须是api.m.mtime.cn_2016072817.log的形式，即一小时为周期的切割。同时时间格式必须为2016072817的方式
'''

import os, logging, time, datetime, socket, json, sys, re, psutil, copy
from configobj import ConfigObj
from pykafka import KafkaClient
from multiprocessing import Process, Queue, Manager


# 日志的格式和输出配置
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log/rtlogtrans-service.log',
                    filemode='a+')

# 这是补日志部分将内容推送至队列中
def pushcontentintoqueue(subsidy_modulename, filename, logoffset1, logoffset2, queue):
    with open(filename, "r") as fn:
        fn.seek(int(logoffset1))
        hostname = socket.gethostname()
        while True:
            line = fn.readline()
            if line != "" and line != "\n":
                line = line.replace("\n", "") + ' "' + hostname + '" \n'
                # 当前时间 秒级别
                timestemp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                curr_position = fn.tell()
                metamessage = {"modulename": subsidy_modulename, "tailed_file": filename,
                               "readfiletime": str(timestemp), "position": curr_position, "subsidylog": 1,
                               "stopflag": 0}
                totalmesg = str(metamessage) + "$!@#$%^&$" + line
                queue.put(totalmesg)
                if curr_position >= int(logoffset2):
                    metamessage = {"modulename": subsidy_modulename, "tailed_file": filename,
                                   "readfiletime": str(timestemp), "position": curr_position, "subsidylog": 1,
                                   "stopflag": 1}
                    totalmesg = str(metamessage) + "$!@#$%^&$" + line
                    queue.put(totalmesg)
                    logging.info(totalmesg)
                    exit(0)

# 补日志部分从队列中拉取内容，并写入到kafka中。
def pullcontentfromqueue(queue, modulename):
    kafkaserver = globalconfig["kafkaserver"]
    # kafka server端ip地址集合
    kafkaserverip = kafkaserver["ipaddress"]
    # 初始化kafka
    kafkaclient = KafkaClient(hosts=kafkaserverip)
    topic = kafkaclient.topics[modulename]
    producer = topic.get_sync_producer()
    while True:
        if not queue.empty():
            try:
                message = queue.get_nowait()
                messagelist = message.split("$!@#$%^&$")
                metamessage = eval(messagelist[0])
                stopflag = metamessage["stopflag"]
                logmessage = messagelist[1]
                if stopflag != 1:
                    producer.produce(logmessage)
                    logging.info(logmessage)
                else:
                    exit(0)
            except Exception,mesg:
                logging.error(mesg)
                exit(1)


# 共享字典进度变量
# 有一种情况是需要考虑的，就是当源日志文件没有打印日志，这个时间是可以不打印持久化日志的，那问题来了，我们补日志的时候是按照时间计算的
# 这个时候就会被纳入补日志的范围内，当轮转到补日志的时候，因为两个时间段内没有日志，所以补的日志为空，这个也是符合逻辑的。
def processdict(modulename, timestemp, persistencefrequency, persistencefile, message):
    global procdict
    if modulename != "":
        if procdict.has_key(modulename):
            # 两个数差额
            value = time.strptime(timestemp, "%Y%m%d%H%M%S")
            temptime = time.strptime(procdict[modulename], "%Y%m%d%H%M%S")
            subsidyflag = message["subsidylog"]
            margin = int(time.mktime(value)) - int(time.mktime(temptime))
            persistencefrequency = int(persistencefrequency)
            # 注意补日志的情况下不持久化文件。
            # 这里假如配置文件写的是60秒，则1分钟持久化一次
            if margin >= persistencefrequency and subsidyflag != 1:
                # 调用函数持久化内容
                tailed_file = message["tailed_file"]
                readfiletime = message["readfiletime"]
                position = message["position"]
                # 拆解每一条日志内容  将模块名 解析出来
                file_message = timestemp + " " + modulename + " " + readfiletime + " " + tailed_file + " " + str(
                    position)
                with open(persistencefile, "a+") as f:  # 直接将持久化文件位置写入持久化函数中，不在做变量传递了
                    # logging.info(message)
                    f.writelines(file_message + "\n")
                    procdict[modulename] = timestemp
        else:
            procdict.setdefault(modulename, timestemp)


# 持久化文件  为什么要将持久化文件暴露出来，是为了解决第一次启动时，要将进度位置持久化进去，而这时消费者的相关参数还没有生成。
def persistence(persistencefile, message):
    with open(persistencefile, "a+") as f:
        # logging.info(message)
        f.writelines(message + "\n")


def killpid(pid):
    pid = int(pid)
    logging.info("psutil kill pid: " + str(pid))
    p = psutil.Process(pid)
    p.kill()



def check_file_validity(file_):
    """ Check whether the a given file exists, readable and is a file """
    if not os.access(file_, os.F_OK):
        logging.fatal("File '%s' does not exist" % (file_))
        return -1
    elif not os.access(file_, os.R_OK):
        logging.fatal("File '%s' not readable" % (file_))
        return -2
    elif os.path.isdir(file_):
        logging.fatal("File '%s' is a directory" % (file_))
        return -3
    else:
        return 0

def readconfig():
    # 读取数据配置文件。
    jsonparams = ""
    moduleslist = ""
    listlen = 0
    with open("config/config_data.json") as jsonfile:
        # 读写应该加锁。或者对json串进行验证，假如不符合格式则直接丢弃，重新获取。
        try:
            jsonparams = json.load(jsonfile)
        except Exception, msg:
            logging.fatal("message in config/config_data.json format error." + str(msg))
    if jsonparams != "":
        moduleslist = jsonparams["moduleslist"]
        logging.info(str(moduleslist))
        listlen = len(moduleslist)
    return listlen, moduleslist


# 生产者
class WriteQueue(object):
    # 日志实时读取并调用writequeue函数
    def __init__(self, queue, modulename, tailed_file, persistencefile):
        # 传递进来的全局队列是将所有读取的日志写入此全局队列中
        self.queue = queue
        # 源模块名
        self.modulename = modulename
        # 源日志文件的绝对路径
        self.tailed_file = tailed_file
        # 持久化文件
        self.persistencefile = persistencefile
        self.try_count = 0

        try:
            self.file_ = open(self.tailed_file, "r")
            self.size = os.path.getsize(self.tailed_file)
            # Go to the end of file
            self.file_.seek(0, 2)
            # 获取文件偏移量
            record_position = self.file_.tell()
            # 第一次运行一定要持久化进度
            # 当前时间 秒级别
            timestemp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            # 当前时间 既是周期性持久化时间  又是读文件时间 格式为： 周期性时间  模块名  读文件时间  源日志文件的绝对路径 偏移量
            file_message = str(timestemp) + " " + self.modulename + " " + str(timestemp) + " " + str(self.tailed_file) + " " + str(record_position)
            # 调用函数持久化内容
            persistence(self.persistencefile, file_message)
        except Exception, mesg:
            logging.fatal("can not read file: " + tailed_file + "mesg: " + str(mesg))
            sys.exit(4)

    def reload_tailed_file(self):
        # Reload tailed file when it be empty be `echo "" > tailed file`, or segmentated by logrotate.
        try:
            self.file_ = open(self.tailed_file, "r")
            self.size = os.path.getsize(self.tailed_file)
            # Go to the head of file
            self.file_.seek(0, 1)
            return True
        except:
            return False

    def follow(self, s=0.01):
        while True:
            # 开始转换文件了
            _size = os.path.getsize(self.tailed_file)
            if _size < self.size:
                while self.try_count < 10:
                    if not self.reload_tailed_file():
                        self.try_count += 1
                    else:
                        self.try_count = 0
                        self.size = os.path.getsize(self.tailed_file)
                        break
                    time.sleep(0.1)
                if self.try_count == 10:
                    logging.fatal("Open %s failed after try 10 times" % self.tailed_file)
                    sys.exit(5)
            else:
                self.size = _size
            # 如何确认上一个文件已经读到结尾了？？
            # 返回文件所在的位置 也就是指针。
            curr_position = self.file_.tell()
            line = self.file_.readline()
            if not line:
                self.file_.seek(curr_position)
            elif not line.endswith("\n"):
                self.file_.seek(curr_position)
            else:
                line = line.replace("\n", "")  + ' "' + hostname +'" \n'
                # 当前时间 秒级别
                timestemp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                metamessage = {"modulename": self.modulename,"hostname":hostname, "tailed_file": self.tailed_file,
                               "readfiletime": str(timestemp), "position": curr_position, "subsidylog": 0}
                totalmesg = str(metamessage) + "$!@#$%^&$" + line
                # logging.info(str(totalmesg))
                # 到这儿程序都是可以的
                print("totalmesg: " + str(totalmesg))
                self.queue.put(totalmesg)

            time.sleep(s)

class TransQueue:
    def __init__(self):
        self.queue = Queue()

    def getQueue(self):
        return self.queue


# 消费者
class ReadQueue():
    def __init__(self, queue, persistencefile, persistencefrequency, modulename):
        self.queue = queue
        self.persistencefrequency = persistencefrequency
        self.persistencefile = persistencefile
        self.modulename = modulename

    # 将持久化作为功能写入 writekafka函数中
    def writekafka(self):
        kafkaserver = globalconfig["kafkaserver"]
        # kafka server端ip地址集合
        kafkaserverip = kafkaserver["ipaddress"]
        # 初始化kafka
        print kafkaserverip
        kafkaclient = KafkaClient(hosts=kafkaserverip)
        topic = kafkaclient.topics[self.modulename]
        with topic.get_producer() as producer:
        # with self.topic.get_sync_producer() as producer:
            metamessage = {"tailed_file":"","readfiletime":"","position":"","subsidylog":0}
            while True:
                # 获取时间的语句一定要写这儿，因为这个时间和从队列中是否能获得到值一点关系没有，但是这句话决定是否需要补日志。
                timestemp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                if not self.queue.empty():
                    message = self.queue.get_nowait()
                    messagelist = message.split("$!@#$%^&$")
                    metamessage = eval(messagelist[0])
                    # logmessage = str(messagelist[1])
                    try:
                        print("message11111111111111111: " + str(message))
                        producer.produce(message)

                    except Exception, mesg:
                        logging.error(mesg)
                        # 将此条信息回写入queue中,保证数据不丢。假如说持久化的那条正好是回填的这条，怎么办？？ 持久化受影响，补日志也会受影响。
                        self.queue.put(message)
                    processdict(self.modulename, timestemp, self.persistencefrequency, self.persistencefile, metamessage)
                else:
                    timestemp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                    # 解决CPU空转，耗费100%CPU的情况
                    processdict(self.modulename, timestemp, self.persistencefrequency, self.persistencefile, metamessage)
                    time.sleep(0.01)


if __name__ == "__main__":

    '''
    开始更改结构：首先利用manager存储模块名和子进程pid，再者将全局唯一的队列改造成一个模块一个队列的方式。将持久化方式改为一个模块一个持久化文件的方式
    while循环 定时取置文件中的内容 然后和正在运行的进程做对比，假如不一致 就进行增删。
    锁是全局锁，是需要交给manager管理的。代码需要改。
    from multiprocessing import Process, Manager

    '''
    # 全局变量记录进度
    procdict = {}
    # 读取全局配置文件
    globalconfig = ConfigObj("config/global_config.ini")
    persistencesection = globalconfig["persistence"]  # persistence持久化
    # 持久化频率
    persistencefrequency = persistencesection["persistencefrequency"]

    if len(sys.argv) == 1:
        '''
        以下代码是解决实时读取日志的需求
        '''
        # 创建全局字典，这里的全局变量是记录的是{"模块名1"：writepid1|readpid1,"模块名2"：writepid2|readpid2}，供配置文件reload使用。
        manager = Manager()
        proc_mesg = manager.dict()
        # 主机名一次性读取就ok，因为主机正式上线后，不会更改主机名。
        hostname = socket.gethostname()
        while True:
            listlen, moduleslist = readconfig()
            # 开始对比全局变量proc_mesg 中变量
            # 1. moduleslist 中包含 而 proc_mesg中不包含  增加
            # 2. moduleslist中包含 而proc_mesg中包含  忽略
            # 3. moduleslist中不包含 而proc_mesg中包含  删除。
            keylist = proc_mesg.keys()
            modulenamefromfile = []
            if listlen != 0:
                for index in xrange(listlen):
                    param_dict = moduleslist[index]
                    modulename = param_dict["modulename"].encode("utf-8")
                    modulenamefromfile.append(modulename)
                logging.info("modulenamefromfile: " + str(modulenamefromfile))
                # 对第一种情况处理
                add_proc = list(set(modulenamefromfile) - set(keylist))
                logging.info("add_proc: " + str(add_proc))
                if len(add_proc) != 0:
                    # 开始创建读实时日志进程
                    for index_add in xrange(len(add_proc)):
                        for index_list in xrange(len(moduleslist)):
                            if moduleslist[index_list]["modulename"] == add_proc[index_add]:
                                logfilepath = moduleslist[index_list]["logfilepath"]
                                filestatus = check_file_validity(logfilepath)
                                if filestatus == 0:
                                    # 持久化文件
                                    persistencefile = "data/" + add_proc[index_add] + ".data"
                                    # 初始化一个队列
                                    transqueue = TransQueue().getQueue()
                                    taillogfile = WriteQueue(transqueue, add_proc[index_add], logfilepath,persistencefile)
                                    process = Process(target=taillogfile.follow, args=())
                                    process.start()
                                    write_processid = process.pid
                                    writekafka = ReadQueue(transqueue, persistencefile, persistencefrequency,add_proc[index_add])
                                    process = Process(target=writekafka.writekafka, args=())
                                    process.start()
                                    read_processid = process.pid
                                    proc_mesg[add_proc[index_add]] = str(write_processid) + "|" + str(read_processid)
                                    logging.info("add_proc[index_add]: " + add_proc[index_add] + " proc_mesg[add_proc[index_add]]: " + str(proc_mesg[add_proc[index_add]]))
                                else:
                                    logging.error(logfilepath + "check file validity fail the status:" + str(filestatus))

                # 对第三种情况处理
                del_proc = list(set(keylist) - set(modulenamefromfile))
                if len(del_proc) != 0:
                    for index_del in xrange(len(del_proc)):
                        pids = proc_mesg[del_proc[index_del]]
                        pidlist = pids.split("|")
                        logging.info(str(pidlist))
                        for index in xrange(len(pidlist)):
                            logging.info("kill pid: " + str(pidlist[index]))
                            killpid(pidlist[index])
                        del proc_mesg[del_proc[index_del]]

            # 1分钟一个周期进行配置文件的读取
            time.sleep(60)

    else:
        '''
        以下代码是解决补日志的需求,记住日志文件格式一定是xxxx年xx月xx日xx小时的格式，别的格式不作处理。
        rtlogtrans.py api.m.mtime.cn /home/mtime/logs/accesslog/api.m.mtime.cn/api.m.mtime.cn_2016070710.log(首) /home/mtime/logs/accesslog/api.m.mtime.cn/api.m.mtime.cn_2016070712.log(末)
        '''
        # 初始化一个队列
        transqueue = TransQueue().getQueue()
        # 这是个数组,假如用户没有排序填写参数，我们执行一遍排序
        # 我们程序相信用户填写时对的。第一个一定是模块名，利用第一个参数的内容去持久化文件中对比，假如存在则进入后续流程，假如找不到 直接写报错日志后退出。
        subsidy_modulename = sys.argv[1]
        sys.argv[2:].sort()  # 掉坑第三次
        subsidy_logfilelist = sys.argv[2:]
        subsidy_lenght = len(sys.argv)
        # 开始获取最开始的时间点和最终的时间点，都是小时级别
        subsidy_pattern = re.compile(r'(\d{10})')
        # 转变成秒  还需要考虑一个问题就是需要判定的是文件的时间匹配，而不是路径中的时间匹配。search().group(0) 返回的是字符串
        subsidy_result = subsidy_pattern.search(os.path.basename(subsidy_logfilelist[0]))
        subsidy_starttime_ymdh = ""
        if subsidy_result is not None:
            subsidy_starttime_ymdh = subsidy_result.group(0)
        subsidy_starttimesecond = ""
        subsidy_endtimesecond = ""
        subsidy_onelogfile = sys.argv[2]
        subsidy_twologfile = ""
        if len(sys.argv[2:]) != 1:
            subsidy_starttime = subsidy_starttime_ymdh + "0000"
            subsidy_starttimesecond = int(time.mktime(time.strptime(subsidy_starttime, "%Y%m%d%H%M%S")))
            # endtime 这儿得说一下,找到则以找到的时间点为准，假如没找到则以endtime时间点为最终结束点。
            subsidy_endtime = subsidy_pattern.search(os.path.basename(subsidy_logfilelist[1])).group(0)
            subsidy_endtime = subsidy_endtime + "5959"
            subsidy_endtimesecond = int(time.mktime(time.strptime(subsidy_endtime, "%Y%m%d%H%M%S")))
            subsidy_twologfile = sys.argv[3]

        # 此判定说明是最近一个小时进行补日志操作,结束时间为当前时间  开始时间为当前这一小时的零分零秒
        elif len(sys.argv[2:]) == 1 and subsidy_starttime_ymdh == "":
            nowtime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            subsidy_starttime = nowtime[0:9] + "0000"
            subsidy_endtime = nowtime
            subsidy_starttimesecond = int(time.mktime(time.strptime(subsidy_starttime, "%Y%m%d%H%M%S")))
            subsidy_endtimesecond = int(time.mktime(time.strptime(subsidy_endtime, "%Y%m%d%H%M%S")))


        # 就是过去的某个时间进行单小时内补日志操作，结束时间为59分59秒，开始时间为这一小时的零分零秒
        elif len(sys.argv[2:]) == 1 and subsidy_starttime_ymdh != "":
            # 假如在一个小时内，模块down后，想补日志：
            # 七层日志是这样的 rtlogtrans.py api.m.mtime.cn /home/mtime/logs/accesslog/api.m.mtime.cn/api.m.mtime.cn_access.log  对于这一种如何补日志？？
            # 模块日志是这种的 rtlogtrans.py payment-gateway-unionpay /home/mtime/logs/payment-gateway-unionpay/2016-07-12/default.log
            subsidy_starttime = subsidy_starttime_ymdh + "0000"
            subsidy_endtime = subsidy_starttime_ymdh + "5959"
            subsidy_starttimesecond = int(time.mktime(time.strptime(subsidy_starttime, "%Y%m%d%H%M%S")))
            subsidy_endtimesecond = int(time.mktime(time.strptime(subsidy_endtime, "%Y%m%d%H%M%S")))

        # 两端的时间点处理完毕，下面就得根据时间算要补日志的源日志文件。然后按照进度文件中的偏移量开始读取源日志文件中的日志入队列了。
        module_pattern = r'^\d{14}\s' + subsidy_modulename
        persistencefile = "data/" + subsidy_modulename + ".data"
        with open(persistencefile, "r") as perfile:
            # 定义时间对比列表
            timecontrast = []
            # 定义存储时间大于两个周期的列表
            timecontraststore = []
            # 因为他要重头查找，所以需要定时对持久化文件的往期日志进行清理（比如5天前的）
            for line in perfile.readlines():
                matchlist = re.findall(module_pattern, line)
                if len(matchlist) != 0:
                    # 获取的持久化文件中的周期性时间
                    rtcyclelogtime = line.split(" ")[0]
                    # 获取持久化文件中的读文件时间
                    rtreadfilelogtime = line.split(" ")[2]
                    # 获取持久化文件中的偏移量
                    rtlogoffset = line.split(" ")[-1].replace("\n", "")
                    # 转换成秒
                    rtlogtimesecond = int(time.mktime(time.strptime(rtcyclelogtime, "%Y%m%d%H%M%S")))
                    if subsidy_starttimesecond <= rtlogtimesecond and rtlogtimesecond <= subsidy_endtimesecond:
                        # 写一个列表 维护两个时间点，当第一个时间点小于第二个时间点 两个及以上周期
                        element = {"rtcyclelogtime": str(rtcyclelogtime), "rtreadfilelogtime": str(rtreadfilelogtime),"rtlogoffset": str(rtlogoffset)}
                        if len(timecontrast) == 0:
                            timecontrast.append(element)
                        else:
                            timecontrast.append(element)
                            '''
                            开始进行两个元素时间部分的对比 类似方式： ['周期性时间|读源日志文件时间|1234', '周期性时间|读源日志文件时间|1234']
                            需要判定两个时间点跨小时和不跨小时是不同的操作方式， 跨小时的判定应该看跨了小时 同时后一个偏移量小于前一个偏移量，这个时候才说明换了文件。没换文件的话继续读。
                            需要考虑杀掉进程后，瞬间启动的情况，小于1个周期如何判定？？ 这部分的实现是这样的：启动首先去持久化文件中查找，当前时间和持久化文件中最新时间是否在一个周期内，假如在，则将偏移量定位在最新时间的偏移量处读取。待开发。
                            '''
                            firstelement_timestemp = int(time.mktime(time.strptime(timecontrast[0]["rtcyclelogtime"], "%Y%m%d%H%M%S")))
                            secondelement_timestemp = int(time.mktime(time.strptime(timecontrast[1]["rtcyclelogtime"],"%Y%m%d%H%M%S")))
                            # 这里采取了 一个周期加1秒的方式来判断他是否中断，此判定方式需要具体讨论。
                            if (secondelement_timestemp - firstelement_timestemp) > (int(persistencefrequency) + 1):
                                # 开始读取读文件时间并判定两个时间的年月日小时是否相同，假如相同表示不跨文件补日志。假如不同是需要跨文件补日志的。
                                timecontraststore.append(timecontrast)  # 来吧，说说列表 append  和 +  区别在哪儿.
                                timecontraststore = copy.deepcopy(
                                    timecontraststore)  # 为什么非得加这一行，不加就不行？？ 为什么必须是deepcopy。
                                # timecontraststore = timecontraststore + timecontrast
                            # 删除第一个元素 这样新进来的元素就会使第二个元素，然后继续进行对比
                            del timecontrast[0]

            for index in xrange(len(timecontraststore)):

                # 需要判定 两个读取源文件时间之间 是否相同  相同的话 这个时候读取的源日志文件就是一个，  不同的话，需要将源日志文件穷举出，然后挨个进行读取 这个时候的读就是正向读取了。
                # 这是 一个列表,列表中是两个字典
                timecontrast_first_rtreadfilelogtime = timecontraststore[index][0]["rtreadfilelogtime"]
                timecontrast_first_rtreadfilelogtime_ymdh = timecontrast_first_rtreadfilelogtime[0:10]
                timecontrast_second_rtreadfilelogtime = timecontraststore[index][1]["rtreadfilelogtime"]
                timecontrast_second_rtreadfilelogtime_ymdh = timecontrast_second_rtreadfilelogtime[0:10]
                # 相同不需要考虑跨文件的情况

                if timecontrast_first_rtreadfilelogtime[0:10] == timecontrast_second_rtreadfilelogtime[0:10]:

                    # 开始对文件进行判定，直接使用的是变量 subsidy_onelogfile 中所指向的文件路径：
                    # 开始获取timecontraststore[index][0] 和timecontraststore[index][1] 中偏移量元素，并调用正向读取函数
                    timecontrast_first_rtlogoffset = timecontraststore[index][0]["rtlogoffset"]
                    timecontrast_second_rtlogoffset = timecontraststore[index][1]["rtlogoffset"]
                    # 开始创建写入queue进程 和读取queue进程，这两个进程在自己分别完成工作后自动退出
                    process = Process(target=pushcontentintoqueue, args=(
                        subsidy_modulename, subsidy_onelogfile, timecontrast_first_rtlogoffset,
                        timecontrast_second_rtlogoffset, transqueue))
                    process.start()
                    process = Process(target=pullcontentfromqueue, args=(transqueue, subsidy_modulename))
                    process.start()


                # 跨文件了，需要穷举有多少个文件
                else:
                    hour = 0
                    processlist = []
                    while True:
                        temp_subsidytime = (datetime.datetime.strptime(timecontrast_first_rtreadfilelogtime, "%Y%m%d%H%M%S") + datetime.timedelta(hours=hour)).strftime("%Y%m%d%H%M%S")
                        temp_subsidytime_ymdh = temp_subsidytime[0:10]
                        hour = hour + 1
                        if int(temp_subsidytime_ymdh) > int(timecontrast_second_rtreadfilelogtime_ymdh):
                            # os._exit(0)
                            sys.exit(0)
                        if temp_subsidytime_ymdh == timecontrast_first_rtreadfilelogtime_ymdh:
                            # 开始提取偏移量，开始从偏移量读取，一直读到结束：
                            timecontrast_first_rtlogoffset = timecontraststore[index][0]["rtlogoffset"]
                            with open(subsidy_onelogfile, "r") as fn:
                                fn.seek(0, os.SEEK_END)
                                position = fn.tell()
                            process = Process(target=pushcontentintoqueue, args=(subsidy_modulename, subsidy_onelogfile, timecontrast_first_rtlogoffset, position,transqueue))
                            process.start()
                            processlist.append(process)
                            process = Process(target=pullcontentfromqueue,args=(transqueue, subsidy_modulename))
                            process.start()
                            processlist.append(process)
                            for index in xrange(len(procdict)):
                                procdict[index].join()
                        elif temp_subsidytime_ymdh == timecontrast_second_rtreadfilelogtime_ymdh:
                            timecontrast_second_rtlogoffset = timecontraststore[index][1]["rtlogoffset"]
                            process = Process(target=pushcontentintoqueue, args=(subsidy_modulename, subsidy_twologfile, 0, timecontrast_second_rtlogoffset, transqueue))
                            process.start()
                            processlist.append(process)
                            process = Process(target=pullcontentfromqueue,args=(transqueue, subsidy_modulename))
                            process.start()
                            processlist.append(process)
                            for index in xrange(len(procdict)):
                                procdict[index].join()

                        else:
                            subsidy_onelogfile_dirname = os.path.dirname(subsidy_onelogfile)
                            subsidy_logfilelist = os.path.basename(subsidy_onelogfile).split(subsidy_starttime_ymdh)
                            temp_subsidy_logfile = subsidy_onelogfile_dirname + "/" + subsidy_logfilelist[0] + temp_subsidytime_ymdh + subsidy_logfilelist[1]
                            with open(temp_subsidy_logfile, "r") as fn:
                                fn.seek(0, os.SEEK_END)
                                position = fn.tell()
                            process = Process(target=pushcontentintoqueue,args=(subsidy_modulename, temp_subsidy_logfile, 0, position, transqueue))
                            process.start()
                            processlist.append(process)
                            process = Process(target=pullcontentfromqueue,args=(transqueue, subsidy_modulename))
                            process.start()
                            processlist.append(process)
                            for index in xrange(len(procdict)):
                                procdict[index].join()


