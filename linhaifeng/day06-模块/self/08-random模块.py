import random

def make_code(n):
    res=''
    for i  in range(n):
        s1=str(random.randint(0,9))
        s2=chr(random.randint(65,90))
        print(s1,s2)
        res+=random.choice([s1,s2])
        print(random.choice([s1]))
    return res
print(make_code(10))