import json

test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
print(test_dict)
print(type(test_dict))
#dumps 将数据转换成字符串
json_str = json.dumps(test_dict)
print(json_str)
print(type(json_str))


new_dict = json.loads(json_str)
print(new_dict)
print(type(new_dict))

with open("./record.json","w") as f:
    json.dump(new_dict,f)
    print("加载入文件完成...")