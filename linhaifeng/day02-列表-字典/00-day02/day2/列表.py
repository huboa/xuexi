my_girl_friends=['alex','wupeiqi','yuanhao',4,10,30]
# my_girl_friends=list(['alex','wupeiqi','yuanhao',4,10,30])


# print(type(my_girl_friends))

# print(my_girl_friends[2])
#
# print(my_girl_friends[1:3])

# my_girl_friends.append('oldboy')
# print(my_girl_friends)

#pop按照索引
# my_girl_friends.pop()
# my_girl_friends.pop()
# my_girl_friends.pop(0)
# my_girl_friends.pop(0)
# my_girl_friends.pop(1)

#remove按照值
# my_girl_friends.remove('yuanhao')
# print(my_girl_friends)


# my_girl_friends.__len__()
# print(len(my_girl_friends))

# print('wupeiqi' in my_girl_friends)
#
# msg='my name is egon111111'
# print('egon' in msg)

#其他操作（掌握）
# my_girl_friends=['alex','wupeiqi','alex','yuanhao',4,10,30]
# my_girl_friends.insert(1,'Sb')
# print(my_girl_friends)




#其他操作（了解）
my_girl_friends=['alex','wupeiqi','alex','yuanhao',4,10,30]
# my_girl_friends.clear()
# print(my_girl_friends)

# l=my_girl_friends.copy()
# print(l)

# print(my_girl_friends.count('alex'))

# my_girl_friends.append('oldboy1')
# my_girl_friends.append('oldboy2')
# my_girl_friends.append('oldboy3')
# print(my_girl_friends)
# my_girl_friends.extend(['oldboy1','oldboy2','oldboy3'])
# print(my_girl_friends)

# print(my_girl_friends.index('alex'))
# my_girl_friends.reverse()
# print(my_girl_friends)

# l=[3,-1,5,2]
# l.sort(reverse=True)
# print(l)



#练习一：
data=['alex',84,[1900,3,38]]
# print(data[0])
# print(data[1])
# print(data[2][0])


# name,age,birth=data
# print(name)
# print(age)
# print(birth)
#
#
# msg='hello'
# a,b,c,d,e=msg
# print(a,b,c,d,e)


# msg='hello'
# a,_,_,_,b=msg
# print(a)
# print(b)

# a,*_,b=msg
# print(a,b)


#队列：先进先出
fifo=[]
#入队
# fifo.append('first')
# fifo.append('second')
# fifo.append('third')
# print(fifo)
# #出队
# print(fifo.pop(0))
# print(fifo.pop(0))
# print(fifo.pop(0))

#入队
# fifo.insert(0,'first')
# fifo.insert(0,'second')
# fifo.insert(0,'third')
# print(fifo)
#
# #出队
# print(fifo.pop())
# print(fifo.pop())
# print(fifo.pop())



#堆栈：先进后出
lifo=[]
