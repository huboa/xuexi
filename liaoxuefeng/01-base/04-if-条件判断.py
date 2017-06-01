#
# #if
# age = 2
# if age >= 18:
#     print('your age is', age)
#     print('adult')
# elif age >=6 :
#     print('your age is', age)
#     print('teenager')
# else:
#     print('kid')
#
# ################
# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')
# ##################
height=1.75
weight=4.5
bmi=weight/(height/weight)
if bmi < 18.5:
    print("too light")
elif bmi <= 25:
    print("stand")
elif bmi <= 28:
    print("too weight")

else:
    print("没法要了")

