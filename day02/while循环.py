# count=0
# while True:
#     print("running",count)
#     count += 1

# count=0
# while count<1000:
#     print("running",count)
#     count += 1

# count=0
# c=0
# zsc_age=20
# while count < 100:
#     print(count)
#
#     if c==3:
#         print("您输入错误已经3次，账户已经被锁定")
#
#     guess_age = input("age>>:")
#     if guess_age.isdigit():
#         guess_age = int(guess_age)
#     else:
#         continue
#
#     if guess_age == zsc_age:
#         print("你真棒！")
#         break
#     elif guess_age > zsc_age:
#         print("猜大了")
#         c += 1
#     else:
#         print("猜小了")
#         c += 1
#
#     count += 1

count=0
zsc_age=20
while count < 3:

    print(count)

    guess_age = input("age>>:")
    if guess_age.isdigit():
        guess_age = int(guess_age)
    else:
        continue

    if guess_age == zsc_age:
        print("你真棒！")
        break
    elif guess_age > zsc_age:
        print("猜大了")
    else:
        print("猜小了")

    count += 1