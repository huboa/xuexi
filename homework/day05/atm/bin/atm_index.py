#!/usr/bin/env python3
#__author__:"shengchong.zhao"

import os
import sys
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_dir)

from core import auth
from core import main
from core import login
from db import DBOpt

if __name__ == '__main__':
     main.start()
# print("name",__name__)