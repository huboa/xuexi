# # L = [ x*x for x in range(10)]
# # L
# # data = ( x*x for x in range(10))
# #
# # for i in data:
# #     print(i)
# #
# #
# # print(data.__next__())
# # print(next(data))
#
# def fib(num):
#     '''
#
#     :param num:求多少个数列 10
#     :return: ###0 1 1 2 3 5 8
#     '''
#     count = 0
#     a,b = 0,1 ##a=0,b=1
#     while count < num:
#         c = a + b
#         a = b
#         b = c
#         #print(a)
#         count+=1
#         yield a   #函数可以退出，返回a 挂起当前函数
# #        return a   #函数执行完退出
#     print("done ....")
# f=fib(100000)  ###生成生成器对象，公式准备完成
#
#
# print(f.__next__())  ###取 yield 返回值
# print(f.__next__())
# print(f.__next__())

def simple(name):
    for i in name:
        yield i
s=simple("zsc")
print(s.__next__())