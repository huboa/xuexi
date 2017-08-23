###update，hexdigest 追加文本

# import hashlib
# m=hashlib.md5()
# m.update('hello'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# print(m.hexdigest())
#
# m=hashlib.md5()
# m.update('helloworld'.encode('utf-8'))
# print(m.hexdigest())
#
# m=hashlib.md5()
# m.update('h'.encode('utf-8'))
# m.update('elloworld'.encode('utf-8'))
# print(m.hexdigest())
#
# with open ('a.xml','rb') as f:
#     for line in f:
#         m.update(line)
#     print(m.hexdigest())
#
# ###加盐
# password='123456'
# m=hashlib.md5('salt'.encode('utf-8'))
# m.update(password.encode('utf-8'))
# password_md5=m.hexdigest()
# print(password_md5)


###hmac
import hmac
h=hmac.new('hello'.encode('utf-8'))
h.update('world'.encode('utf-8'))
print(h.hexdigest())
h=hmac.new('hello'.encode('utf-8'))
h.update('wor'.encode('utf-8'))
h.update('ld'.encode('utf-8'))
print(h.hexdigest())
#####头必须一样，后面和md5 一样
h=hmac.new('hell'.encode('utf-8'))
h.update('world'.encode('utf-8'))
print(h.hexdigest())