import os
import sys

base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)
sys.path.append("../atm")
#import
print(sys.path)
for n in (sys.path):
    print(n)

