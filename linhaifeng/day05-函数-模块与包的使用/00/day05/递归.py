#递归调用：在调用一个函数的过程中，直接或间接地调用了函数本身

#直接
# def func():
#     print('from func')
#     func()
#
# func()

#间接
# def foo():
#     print('from foo')
#     bar()
#
# def bar():
#     print('from bar')
#     foo()
#
# foo()


#
# age(5)=age(4)+2
# age(4)=age(3)+2
# age(3)=age(2)+2
# age(2)=age(1)+2
# age(1)=18

# age(n)=age(n-1)+2 #n>1
# age(1)=18 #n=1

# def age(n):
#     if n == 1:
#         return 18
#     return age(n-1)+2
#
# print(age(5))

#递归的执行分为两个阶段：
#1 递推
#2 回溯


# l =[1, 2, [3, [4, 5, 6, [7, 8, [9, 10, [11, 12, 13, [14, 15,[16,[17,]],19]]]]]]]
#
# def search(l):
#     for item in l:
#         if type(item) is list:
#             search(item)
#         else:
#             print(item)
#
# search(l)
#





# #二分法
# l = [1,2,5,7,10,31,44,47,56,99,102,130,240]
#
#
# def binary_search(l,num):
#     print(l) #[10, 31]
#     if len(l) > 1:
#         mid_index=len(l)//2 #1
#         if num > l[mid_index]:
#             #in the right
#             l=l[mid_index:] #l=[31]
#             binary_search(l,num)
#         elif num < l[mid_index]:
#             #in the left
#             l=l[:mid_index]
#             binary_search(l,num)
#         else:
#             print('find it')
#     else:
#         if l[0] == num:
#             print('find it')
#         else:
#             print('not exist')
#         return
#
# binary_search(l,32)

















#二分法
l = [1,2,5,7,10,31,44,47,56,99,102,130,240]


def binary_search(l,num):
    print(l)
    if len(l) == 1:
        if l[0] == num:
            print('find it')
        else:
            print('not exists')
        return
    mid_index=len(l)//2
    mid_value=l[mid_index]
    if num == mid_value:
        print('find it')
        return
    if num > mid_value:
        l=l[mid_index:]
    if num < mid_value:
        l=l[:mid_index]
    binary_search(l,num)

binary_search(l,32)


























