import os
print(os.listdir('.'))
print(os.stat('04-eval-与compile.py'))
print(os.sep)
print(os.linesep)
print(os.pathsep)
print([os.sep,os.linesep,os.pathsep])


os.system('ls .')

print(os.path.dirname(r'cdadsf/adsfa/asdf'))
print(os.path.basename((r'cdadsf/adsfa/asdf')))