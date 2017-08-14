cmd='print(x)'
x=1
eval(cmd)

eval(cmd,{"x":0},{'y':1000})



code=compile(cmd,'','exec')
exec(code)
tag=" "
print(tag.join(['egon','say','hello','world']))
print(type(tag.join(['egon','say','hello','world'])))
name='egon'
print(name.center(30,'-'))
print(name.ljust(30,'*'))
print(name.rjust(30,'*'))
print(name.zfill(50))