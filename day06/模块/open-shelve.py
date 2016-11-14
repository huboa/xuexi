import shelve


f = shelve.open('12345')
print(f["test"])
print(f["info"])
# print(f["func"])("test",30)