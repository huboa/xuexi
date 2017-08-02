#模块只在第一次导入时才会执行，之后的导入都是直接引用内存已经存在的结果
import sys
print('spam' in sys.modules) #存放的是已经加载到内的模块


import spam
print('spam' in sys.modules)
# import spam
# import spam
# import spam
# import spam
# import spam