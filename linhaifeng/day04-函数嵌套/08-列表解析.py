l=[]
for i in range(10):
    if i >= 5:
        l.append("egg%s" %i)

print(l)

l=["egg%s" %i for i in range(10)]
print(l)

l1=["egg%s" %i for n in range(9)  if i>=5 ]
print(l1)
nums=[1,2,3,4,5,6]

nums_new=[item**2 for item in nums if item >= 3]
print(nums_new)

###列表生成器
l=("egg%s" %i for i in range(10))
print(l)