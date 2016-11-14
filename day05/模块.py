import os
import sys

os.path.abspath ##绝对路径
base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dir =os.path.abspath(__file__)

print(dir)
dir=os.path.dirname(__file__)
print(dir)

dir=os.path.dirname(os.path.dirname(__file__))
print(dir)

dir=os.path.dirname(os.path.dirname(os.path.dirname(__file__))) ###剥去两个目录
print(dir)

sys.path.append(base_dir) ###添加路径
print(sys.path)
