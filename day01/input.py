name =input("name:")
age = input("age:")
job = input("job:")
hobby = input("hobby:")

print("My name is",name,"I am ",age,"years old","my job is ",job,"My hobby is",hobby)

info = '''
------info of %s ------
Name: %s
Age : %s
Job : %s
Hobby:%s
=======end ========
'''%(name,name,age,job,hobby)

print(info)