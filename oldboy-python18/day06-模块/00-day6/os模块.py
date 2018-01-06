import os

# print(os.listdir('.'))

# print(os.stat('m1.py').st_size)

# print(os.sep)
# print(os.linesep)
# print(os.pathsep)

# print([os.sep,os.linesep,os.pathsep])

# res=os.system('dir .')
# print('====?>',res)

# print(os.path.dirname(r'C:\a\b\c\d\a.txt'))
# print(os.path.basename(r'C:\a\b\c\d\a.txt'))
# print(os.path.split(r'C:\a\b\c\d\a.txt'))

# print(os.stat('m1.py').st_atime)
# print(os.stat('m1.py').st_size)
# print(os.path.getsize('m1.py'))


# print(os.path.join('C:\\','a','b','c','d.txt'))
# print(os.path.join('C:\\','a','b','D:\\','c','d.txt'))

# print(os.path.normcase('c:/wiNdows\\system32\\')  )

# print(os.path.normpath('c://wIndows\\System32\\../Temp/')  )

# a='/Users/jieli/test1/\\\a1/\\\\aa.py/../..'
# print(os.path.normpath(a))


print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BASE_DIR=os.path.normpath(os.path.join(
    os.path.abspath(__file__),
    '..',
    '..'
)
)
print(BASE_DIR)






