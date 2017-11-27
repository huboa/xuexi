import shelve


f = shelve.open('12345')
print(f["day06"])
print(f["info"])
# print(f["func"])("day06",30)