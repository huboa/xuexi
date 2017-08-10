import  re
expression1='1-2*(60+2*-3))'

print('express1', expression1)
content = re.search('\(([\-\+\*\/]*\d+\.?\d*)*\)', expression1).group()

expression_old = content
content = content.strip('()')
print('''=====-------''',content)
print(expression_old,'old_expression')

expression1 = expression1.replace(expression_old, content)
print(expression1, '=====')

