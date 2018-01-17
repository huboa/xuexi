import s1 # 找到s1模块进行解释
import s2 # 找到s2模块进行解释，找到最开始时创建的那个对象，并打印

print("s3打印",s1.site) # 找到最开始时创建的那个对象，并打印
print(s1.site.registry)