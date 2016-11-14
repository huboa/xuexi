import shelve

d = shelve.open('12345')##打开一个文件

def stu_data(name,age):
    print("register stu",name,age)

name = ["a","b","c"]
info = {"name":"zsc","age":22}
d["test"] = name #持久化
d["info"] = info
d["func"] = stu_data("zsc",22)

