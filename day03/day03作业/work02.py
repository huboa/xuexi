# 1、查
#     输入：www.oldboy.org
#     获取当前backend下的所有记录
#
# 2、新建
#     输入：
#         arg = {
#             'bakend': 'www.oldboy.org',
#             'record':{
#                 'server': '100.1.7.9',
#                 'weight': 20,
#                 'maxconn': 30
#             }
#         }
#
# 3、删除
#     输入：
#         arg = {
#             'bakend': 'www.oldboy.org',
#             'record':{
#                 'server': '100.1.7.9',
#                 'weight': 20,
#                 'maxconn': 30
#             }
#         }
#
import  os,re,sys
from collections import defaultdict,OrderedDict
conf = "haproxy.cfg"
conf_new = "haproxy.cfg.new"
backend_list = []
server_dict= {}
show_dict = {}
backend_name_dict = {}
server_info= []
server_flag = False                                                     ###初始化server判断标志位###
with open(conf,'r') as ha:                                             ###打开haproxy配置文件###
    for line in ha:
        line = line.strip('\n')
        if re.match('backend',line):                                    ###匹配配置文件以backend开头的行###
            backend_name = re.split('\s+',line)[1]
            backend_list.append(backend_name)
            server_info1 = []
            server_flag = True                                           ###赋值标志位为真，用来与server关联###
        elif server_flag and re.match('\s+server',line):               ###匹配配置文件以server开头的行###
            server_info = re.split('\s+',line)
            server_info.remove('')
            server_info1.append(server_info)
            server_dict['server'] = server_info[1]
            server_dict['weight'] = server_info[4]
            server_dict['maxconn'] = server_info[5]
            backend_name_dict[backend_name] = "name"
            backend_name_dict[backend_name] = server_info1
        else:
            server_flag = False

#循环
options_list = ["1.查询backend","2.删除backend","3.新增backend","5.退出"]
while True:
      for i in options_list:
        print(i)
      find = (input("\033[94m请选择操作条目序号：\033[0m"))
      if find.isdigit():
            find = int((find))
            #1是查询
            if find == 1:
               for i, ele in enumerate(backend_list):
                   print(i, ele)
               find1 = input("请输入您要查询的backend的序号：")
               find1 = int(find1)
               for j in range(1):
                   print("==========%s============" %backend_list[find1])
                   for i in backend_name_dict[backend_list[find1]]:
                      print("server %s weigt %s maxconn %s" %(i[1],i[3],i[5]))
            #2是删除
            elif find == 2:
               for i, ele in enumerate(backend_list):
                       print(i, ele)
               find3 = int(input("请选择您要删除backend的序号："))
               server_show = []
               for i, ele in enumerate(backend_name_dict[backend_list[find3]]):
                               server_show.append("server %s weight %s maxconn %s" % (ele[1], ele[3], ele[5]))
                               print(i, "server %s weight %s maxconn %s" % (ele[1], ele[3], ele[5]))
                               server_show1= str(server_show[0])
                               print(server_show1)
                               f = open(conf, "r")
                               f1 = open(conf_new, "a+")
                               for i in f:
                                   if server_show1 in i:
                                       i = i.replace(server_show1, "")
                                   f1.write(i)
                                   f1.flush()
                               f.close()
                               f1.close()
                               os.remove(conf)
                               os.rename(conf_new, conf)
                               backend_list1 = []
                               backend_list1.append("backend %s" %(backend_list[find3]))
                               backend_list2 = str(backend_list1[0])
                               f = open(conf, "r")
                               f1 = open(conf_new, "a+")
                               for i in f:
                                   if backend_list2 in i:
                                       i = i.replace(backend_list2, "")
                                   f1.write(i)
                                   f1.flush()
                               f.close()
                               f1.close()
                               os.remove(conf)
                               os.rename(conf_new, conf)
                               print("删除成功！！！")
            #3是增加
            elif find == 3:
                   arg = []
                   backend_name1 = []
                   backend_list3 = []
                   input_back = input("\033[94m请输入backend(www.orgboy.org):\033[0m")
                   arg.append("backend %s" %input_back)
                   input_server = input("\033[94m请输入server(127.0.0.1):\033[0m")
                   input_weight = input("\033[94m请输入weight(20):\033[0m")
                   # arg["weight"] = input_weight
                   input_maxconn = input("\033[94m请输入maxconn(3000):\033[0m")
                   arg.append("        server %s weight %s maxconn %s" %(input_server,input_weight,input_maxconn))
                   backend_name1 = str(arg[0])
                   f = open(conf, "a+")
                   f.write("%s \n" %backend_name1)
                   f.flush()
                   f.close()
                   backend_list3 = arg[1]
                   backend_list3 = str(backend_list3)
                   f = open(conf, "a+")
                   f.write("%s \n" %backend_list3)
                   f.close()
                   print("添加成功！！！")
            #5是退出
            elif find == 5:
               exit()
      else:
          print("\033[91m请输入正确的序号\033[0m")
          continue