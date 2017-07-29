###结论
#内存--》》内置 --》》硬盘中sys.path

import sys
print(sys.path)
print(type(sys.path))

sys.path.append("/Users/ZSC/git/xuexi-mac/linhaifeng/day05-函数-模块与包的使用/模块/aaa")

print(__name__)