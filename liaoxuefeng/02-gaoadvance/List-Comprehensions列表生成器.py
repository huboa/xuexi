
#生成列表  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L=list(range(1,11))
print(L)
print(list(range(1,11)))

#生成列表 [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([x * x for x in range(1, 11)])

##生成列表['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
print( [m + n for m in 'ABC' for n in 'XYZ'])

##生成列表 筛选出仅偶数的平方
print( [x * x for x in range(1, 11) if x % 2 == 0])

# 显示.目录  os.listdir可以列出文件和目录
import os
print([d for d in os.listdir('./')])

#字典生成列表
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k,v in d.items():
    print(k,'=',v)
print([k +'=' + v for k, v in d.items()])

##列表变更成小写
L = ['Hello', 'World', 'IBM', 'Apple','15',44]
print([s.lower() for s in L if  isinstance(s,str)])
