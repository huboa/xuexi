# g = (x * x for x in range(10))
#
# for n in g:
#     print(n)

##generator保存的是算法
# def fib(max):
#          n, a, b = 0, 0, 1
#
#          while n < max:
#              print(b)
#              a,b = b,a+b
#              n = n + 1
#
#          return 'done'
# fib(8)

###
def fib(max):
    n, a, b = 0, 0, 1

    while n < max:
        yield b
        a,b = b,a+b
        n = n + 1

    return 'done'

for n in fib(9):
    print(n)

    