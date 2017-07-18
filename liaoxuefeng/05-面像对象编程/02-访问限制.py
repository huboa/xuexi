class Student(object):
    def __init__(self, name, score):
        self.__name = name           ###name 加上横线就变成了private 私有变量,只有内部可以访问，外部不能访问
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):      ###提供了新的方法供外部读取
        return self.__name
    def get_score(self):
        return self.__score

    def set_score(self, score):  ###提供了新的方法供外部写入
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

zsc=Student("赵胜冲",22)
bart = Student('Bart Simpson', 59)

print(zsc.get_name()) ####直接调用名字胡方法被限制,只能用get_name 获取了

###如果非要访问 可以直接
print(bart._Student__name)
