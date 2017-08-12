import hashlib
m=hashlib.md5()
m.update('hello'.encode('utf-8'))
m.update('world'.encode('utf-8'))
print(m.hexdigest())

m=hashlib.md5()
m.update('helloworld'.encode('utf-8'))
print(m.hexdigest())

m=hashlib.md5()
m.update('h'.encode('utf-8'))
m.update('elloworld'.encode('utf-8'))
print(m.hexdigest())