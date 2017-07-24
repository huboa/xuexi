'''
oldboy_age = 20

for i in range(10):

    guess_age = int(input("age:"))

    if guess_age == oldboy_age:
        print("正确！")
        break
    elif guess_age > oldboy_age:
        print("大了，请重试！")
    else :
        print("小了，请重试！")



for i in range(10):
    print(i)
else:
    print("loop is done!")





for i in range(10):
    for j in range(10):

        if i < 6:
            #break   ###跳出当前层循环
            continue ##跳出当次循环继续下一次
        print(i, j)
'''

for i in range(10):

    if i == 6:
         #break   ###跳出当前层循环
        continue  ##跳出当次循环继续下一次

    print(i)
else:
    print("loop is done!")