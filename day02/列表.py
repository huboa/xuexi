names = ["one","two","three"]

##增
# names.append("four")
# print(names)
#
# names.insert(2,"insert")
# names.insert(1,"insert")
#
# print(names)
# ##删
# names.remove("insert")
# print(names)
# del names[1]
# print(names)
# print(names.pop())
# print(names)
# ##改
#
# names[2] = "中文"
# print(names)

#
# ##查
# print(names[-2])
# print(names[0::2])
# print(names[-3:])###get the last 3
# print(names[:3]) ##get the first 3
# print(names.index("中文")) ##找索引下标
#
# print(names[1])
#
# print("one count=",names.count("one"))
names=["111","2222","ttet"]
#names.extend(n2)
#print(names,n2)
#
# names.sort()
# print(names)
# names.reverse()
# print(names)
# names.pop()
# print(names)
#
#
#
# n3 = names.copy()
# n4 = names
# print(n3,id(names),id(n3))
# print(n4,id(names),id(n4))
#
# names.pop()
# print("----------")
# print(n3,id(names),id(n3))
# print(n4,id(names),id(n4))

for i,ele in enumerate(names):
    print(i[0],i[1])
    print(i,ele)