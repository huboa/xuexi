##小九九
n = 9
i = 0
while (i < n):
    i += 1
    j = 0
    L = []
    while(j < i):
         j += 1
         s = j * i
         # print(j,"*",i ,"=",s)
         L.append("%s*%s=%s"%(j,i,s))


    print(L)


##汉诺塔
# def move(n,a,b,c):
#     if n==1:
#         print(a,'->',c)
#     else:
#         move(n-1,a,c,b)
#         move(1,a,b,c)
#         move(n-1,b,a,c)
#
# move(5,"A","B","C")