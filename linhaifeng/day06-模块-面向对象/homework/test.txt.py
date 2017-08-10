import re
print(re.sub('([\d+\.?\d*])\*([\d+\.?\d*])',r'\2\1','60+2*-3'))