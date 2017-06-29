

#####手动定义my_abs函数
# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs(-3))


##空函数
# def nop():
#     pass


###异常处理
# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
# # print(abs('A'))
# print(my_abs('A'))

###返回多个值
import math

# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
# y = move(100,200,4,math.pi / 6)
# x, y = move(100, 100, 60, math.pi / 6)
# print(x,y)


####练习题 quadratic(a, b, c)，接收3个参数，返回一元二次方程
import math
def  quadratic(a, b, c):
    if b**2-4*a*c==0:
        x=-c/b
        return x
    elif b**2-4*a*c<0:
        return 'N/A'
    else:
        x1=2*c/(-b-math.sqrt(b**2-4*a*c))
        x2=2*c/(-b+math.sqrt(b**2-4*a*c))
    return x1,x2

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
print(quadratic(1, 0, 8))

