import json
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
print(base_dir)
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(base_dir)
sys.path.append(base_dir)

# def  saveDB(id,userdict):
#     f = open(id, "w", encoding="utf-8")
#     f.write(json.dumps(userdict))
#     f.close()

def read_conf():
    file_path = '../conf/server.ini'
    config = ConfigParser.ConfigParser()
    config.read(file_path)
    return config.get('conf', 'value')


def readDB(id):
    file_path = '../db/%s' % id
    user_list=json.load(open(file_path,"r"))
    # print(file_path)
    # print(list)
    return user_list
#
#print(readDB("1235"))
# userdict = {
#     'id': 1235,
#     'password': 'abc',
#     'credit': 15000,
#     'balance': 15000,
#     'enroll_date': '2016-01-02',
#     'expire_date': '2021-01-01',
#     'pay_day': 22,
#     'status': 0  # 0 = normal, 1 = locked, 2 = disabled
# }

#print(userdict())

 # id="1235"
# saveDB(id,userdict)
#
# readDB(id)
#print(json.load(open(id,"r")))