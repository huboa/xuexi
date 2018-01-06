import configparser

config=configparser.ConfigParser()
config.read('a.ini')

#取配置
# print(config.sections()) #看标题
# print(config.options(config.sections()[0])) #查看某个标题下的配置项
# res=config.get('alex','name')#查看某个标题下的某个配置项的值
# print(type(res))

# res1=config.getint('egon','age')#查看某个标题下的某个配置项的值
# print(type(res1))
#
# res1=config.getboolean('egon','is_admin')#查看某个标题下的某个配置项的值
# print(type(res1))
#
# res1=config.getfloat('egon','salary')#查看某个标题下的某个配置项的值
# print(type(res1))


#修改
# config.remove_section('alex')
# config.remove_option('egon','age')

config.add_section('alex')
config.set('alex','name','SB')


config.write(open('a.ini','w'))




