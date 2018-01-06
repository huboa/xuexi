# import settings
#
# class MySql:
#     def __init__(self,host,port):
#         self.host=host
#         self.port=port
#
#     @classmethod
#     def from_conf(cls):
#         print(cls)
#         # return cls(settings.HOST,settings.PORT)
#
#     def func1(self):pass
#
#
# conn1=MySql('127.0.0.1',3306)

# print(MySql.from_conf)
# conn2=MySql.from_conf()

# print(conn1.host,conn2.host)

# print(conn1.func1)
# print(conn1.from_conf)
# print(MySql.from_conf)


# conn1.from_conf()
# MySql.from_conf()








import settings
import uuid
class MySql:
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.id=self.create_id()

    # @classmethod
    # def from_conf(cls): #绑定给类的
    #     print(cls)
    #     # return cls(settings.HOST,settings.PORT)
    #
    # def func1(self): #绑定给对象的
    #     pass

    @staticmethod
    def create_id(): #非绑定方法
        return str(uuid.uuid1())


conn1=MySql('127.0.0.1',3306)
conn2=MySql('127.0.0.2',3306)
conn3=MySql('127.0.0.3',3306)
# print(MySql.create_id)
# print(conn1.create_id)

print(conn1.id,conn2.id,conn3.id)