import pickle
import os
class School(object):
    def __init__(self,school_name):
        self.school_name = school_name

    def create_teacher(self,school_name,teacher_name,age,sex):
        teacher_data = [school_name,teacher_name,age,sex]
        return teacher_data

    def create_lesson(self,school_name,lesson_name,price,cycle):
        lesson_data = [school_name,lesson_name,price,cycle]
        return lesson_data


class Classes(object):
    def __init__(self,classes_name):
        self.classes_name = classes_name


class Lesson(object):
    def __init__(self, lesson_name, price, cycle):
        self.lesson_name = lesson_name
        self.price = price
        self.cycle = cycle

class Schoolmember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

class Teacher(Schoolmember):
    def __init__(self,name,age,sex):
        super(Teacher,self).__init__(name,age,sex)

class Student(Schoolmember):
    def __index__(self,name,age,sex):
        super(Student,self).__init__(name,age,sex)


def pickle_wb(file_name,data):
    f = open(os.path.dirname(os.path.dirname(__file__))+"\\"+"db"+"\\"+file_name,"wb")
    f.write(pickle.dumps(data))
    f.close()
    return


def pickle_rb(file_name):
    f = open(os.path.dirname(os.path.dirname(__file__))+"/"+"db"+"/"+file_name,"rb")
    try:
        data = pickle.loads(f.read())
    except EOFError:
        data = []
    return data
