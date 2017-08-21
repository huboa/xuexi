##打开文件
import configparser
config=configparser.ConfigParser()
config.read('a.ini')


####读取
###查看 sections,options
# print(config.sections())  ##查看标题
# print(config.options(config.sections()[0]))  #查看选项下的key
# print(config.get(section='zsc',option='name'))##查看具体项的值
# print(config.get('zsc','name')) ##简单写法
#
# ##取制定类型get,getint,getboolean,getfloat
# res=config.get('zsc','age')  ##取值默认为str
# res=config.getint('zsc','age')####取整形
# res=config.getboolean('zsc','is_admin') ##取布尔类型
# res=config.getfloat('zsc','salary')  #取浮点型
# print(res,type(res))

####删除 remove_section,remove_option
# config.remove_section('zxx') ###删除标题
# config.remove_option('zsc1','name')##删除选项

####增加  标题和选项，add_section,set
# config.add_section('zsc5')###添加标题
# config.set('zsc5','name','zhaoshengchong')  ###依赖标题必须存在

###修改  可以先删除再添加
config.remove_option('zsc','name')
config.set('zsc','name','zsc')

###保存
config.write(open('a.ini','w'))###保存文件




