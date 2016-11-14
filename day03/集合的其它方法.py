###集合的更新
s1={1,2,3}
s1.update("e")
s1.update((1,2,3,4))
s2={"h","e",1}
s1.update(s2)
s1.update("hello")
print(s1)


##整体添加
s1.add("hello")
print(s1)

###随机删除
s1.pop()
print(s1)

##指定删除一个参数不存在报错
s1.remove("e")
s1.remove("o")
print(s1)
##删除不存在不报错
s1.discard("p")
print(s1)
##清空
s1.clear()
##
s1={1,2,3,"a","e"}
s2={1,2,3}
s1.difference_update(s2)
print(s1)