import re
expression1='1-2*((60+2*(-3-40.0/0.5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

#print(re.search('\(([\-\+\*\/]*\d+\.?\d*)*\)',expression1))
print(re.search('\(([\-\+\*\/]?\d+\.?\d*)*\)',expression1))