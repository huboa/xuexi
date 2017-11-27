# # py_list=["alex","zsc","zxx","zhangsan"]
# # linux_list=['zsc','zxx']
# # both=[]
# #
# # for name in linux_list:
# #     if name in py_list:
# #         both.append(name)
# #
# # print(both)
# #
# # s1={'a',1,2,3,4,3,4,3}    ###集合去重概念
# #
# # print(s1)
#
#
# py_set={"alex","zsc","zxx","zhangsan"}
# linux_set={'zsc','zxx'}
# s3={"zsc"}
# ###交集合
# print(py_set&linux_set)
# print(py_set.intersection(linux_set).intersection(s3))
#
# ###并集
# print(py_set|linux_set)
# print(py_set.union(linux_set).union(s3))
# ###差集
#
# print(py_set-linux_set)
# print(py_set.difference(linux_set).difference(s3))
#
# ###对称差集
#
# print(py_set^linux_set)
# print(py_set.symmetric_difference(linux_set))
#
# ###子集
#
# print(py_set<=s3)
# print(py_set.issubset(s3))
# print(s3<=py_set)
# print(s3.issubset(py_set))
#
#
# ###父集
# print(s3>=py_set)
# print(s3.issuperset(py_set))

# ###集合取值用处不大
# s3={1,2,3,"a"}
# print("a" in s3)
# for i in s3:
#     print(i)
####元祖的作用

t1=(1,2,3)
print(t1)
s3=set()
s4=set("hello")
s5=set(("asere","asdf",123,12,12434,2123,12))
print(s4)
print(s5)