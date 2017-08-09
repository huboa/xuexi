import random
# print(random.sample([1,'23',[4,5]],2))
#
# print(random.uniform(1,3))

#
# item=[1,3,5,7,9]
# random.shuffle(item)
# print(item)



def make_code(n):
    res=''
    for i in range(n):
        s1=str(random.randint(0,9))
        s2=chr(random.randint(65,90))
        res+=random.choice([s1,s2])
    return res
print(make_code(10))