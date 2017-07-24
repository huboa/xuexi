# l=[]
# for i in range(10):
#     if i >=5:
#         l.append('egg%s' %i)
#
# print(l)

#列表解析
# for i0 in ...:
#     if 条件1:
#         for i1 in ...:
#             if 条件2:
#                 for i2 in ...:
#                     if 条件3:
#                         。。。

# l=['egg%s' %i for i in range(10)  if i >=5]
# print(l)

# nums=[1,2,3,4,5,6]
# nums_new=[item**2 for item in nums if item > 3]
# print(nums_new)


# nums_new=[]
# for item in nums:
#     nums_new.append(item**2)
#
# print(nums_new)


# names=['alex_sb','wupeiqi_sb','egon','yuanhao_sb']
#
# names_new=[name for name in names if name.endswith('sb')]
# print(names_new)
