import json
import demjson
with open("./temp_subject.json",'r') as load_f:


    load_dict = json.load(load_f)
    print(load_dict,)
    print(type(load_dict))
for n in load_dict["subject_list"]:
    print(n)