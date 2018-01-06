import hashlib
#
# m=hashlib.md5()
# m.update('hello'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# print(m.hexdigest())
#
#
# m=hashlib.md5()
# m.update('helloworld'.encode('utf-8'))
# print(m.hexdigest())
#
# m=hashlib.md5('helloworld'.encode('utf-8'))
# print(m.hexdigest())
#
#
# m=hashlib.md5('h'.encode('utf-8'))
# m.update('elloworld'.encode('utf-8'))
# print(m.hexdigest())
# m=hashlib.md5()
# with open('a.xml','rb') as f:
#     for line in f:
#         m.update(line)
# print(m.hexdigest())
#
#
# #耗费内存不推荐使用
# m=hashlib.md5()
# with open('a.xml','rb') as f:
#     m.update(f.read())
# print(m.hexdigest())





#加盐
# password='alex3714'
# m=hashlib.md5('yihangbailushangqingtian'.encode('utf-8'))
# m.update(password.encode('utf-8'))
#
# passwd_md5=m.hexdigest()
#
# print(passwd_md5)



import hmac

h=hmac.new('hello'.encode('utf-8'))
h.update('world'.encode('utf-8'))
print(h.hexdigest())

h=hmac.new('hello'.encode('utf-8'))
h.update('w'.encode('utf-8'))
h.update('or'.encode('utf-8'))
h.update('ld'.encode('utf-8'))
print(h.hexdigest())