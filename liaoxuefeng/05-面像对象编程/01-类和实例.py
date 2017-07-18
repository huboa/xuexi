###类就是一个模版
class Student(object):
    def __init__(self, name, score):  ###定义一个特殊的__init__方法  self 代表实例本身
        self.name = name
        self.score = score

    def print_score(std):
        print('%s: %s' % (std.name, std.score))

    def get_grade(self):  #增加新方法后
        if self.score >= 90:
                return 'A'
        elif self.score >= 60:
                return 'B'
        else:
                return 'C'

zsc=Student("赵胜冲",22)
bart = Student('Bart Simpson', 59)
#
# print(zsc)
# print(zsc.name)
# print(zsc.get_grade())
# print(bart.name,bart.score,bart.get_grade(),"####")

# print('%s: %s' % (zsc.name,zsc.score))

zsc.print_score()   ####类的封装 直接访问类的方法 就是数据封装
print(zsc.get_grade())
print(bart.get_grade())



