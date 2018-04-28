class File:

    def file_add():
        pass

    def file_del():
        pass

    def file_update():
        pass

class Db:
    def __init__(self,host,ip,port,user,pwd):
        self.host =host
        self.ip =ip
        self.port =port
        self.user =user
        self.pwd =pwd

    def db_add(self,sql):
        self.host

    def db_del(self,sql):
        pass

    def db_update(self,sql):
        pass

class Log:
    def log_add():
        pass

    def log_del():
        pass

obj = Db('1.1.1.1','111111',3306,'user','xx')
obj.db_add('insert into ....')
