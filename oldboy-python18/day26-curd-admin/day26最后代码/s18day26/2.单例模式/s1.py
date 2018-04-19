# 创建类
class BlSite(object):
    def __init__(self):
        self.registry = {}
        self.registry = {'k0':1}

    def add(self,k,v):
        self.registry[k] = v
        return self.registry[k]

# 实例化对象
site = BlSite()
# print(site.add("k1","v1"))