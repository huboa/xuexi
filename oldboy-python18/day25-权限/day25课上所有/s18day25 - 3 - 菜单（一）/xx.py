
v1 = '^/users/$'

current_url = "/users/"


import re

result = re.match(v1,current_url)
print(result)