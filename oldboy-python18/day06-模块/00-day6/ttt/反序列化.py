import shelve

obj=shelve.open(r'sheve.shl')

# print(obj['alex'])
# print(obj['egon'])

# obj.close()

for i in obj:
    print(i,obj[i])