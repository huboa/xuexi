
def calc(n):
    # if n > 5:
    #     print("hello")
    n=n*2
    return n*n

#print(calc(6))
map(calc(),[1,2])

###匿名函数lambda
data = map(lambda n:n*2,[1,2])
print(data)

data = map(lambda n:n*2,range(10))
print(data)


for n in data:
    print(n)

data = map(lambda n:n*n,range(10))

###3元运算
a = 4
b = 5
d =a if a >10 else b

print(d)