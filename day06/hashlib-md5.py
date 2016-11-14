import hashlib
import os
import sys
import time
m = hashlib.md5()
m.update(b"zsc")
print(m.hexdigest())
m.update(b"zz")
print(m.hexdigest())

m2 = hashlib.md5()
m2.update(b"zsczz")
print(m2.hexdigest())

import hmac

h_obj=hmac.new(b"salt",b"hello")##网络的消息加密传输
print(h_obj.hexdigest())
print(type(h_obj))
print(hmac)