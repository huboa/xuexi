def add(x,y,f):
    return f(x) + f (y)

def calc(n):
    return n+1

res = add(3,-6,abs)
print(res)
res = add(3,-6,calc)
print(res)