###多继承
class Permission(object):
    def get_add(self):
        return True

class Base(object):
    def get_add(self):
        return False


class UserConfig(Permission,Base):

    def show(self):
        v = self.get_add()
        print(v)
        
obj = UserConfig()
obj.show()