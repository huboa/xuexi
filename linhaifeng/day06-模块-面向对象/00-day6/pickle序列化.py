import pickle

# dic={'name':'egon','age':18}
#
# print(pickle.dumps(dic))
# with open('d.pkl','wb') as f:
#     f.write(pickle.dumps(dic))

# with open('d.pkl','rb') as f:
#     dic=pickle.loads(f.read())
#     print(dic['name'])

# dic={'name':'egon','age':18}
# pickle.dump(dic,open('e.pkl','wb'))


# print(pickle.load(open('e.pkl','rb'))['name'])



#

def func():
    print('from func')


# import json
# print(json.dumps(func))

import pickle
# print(pickle.dumps(func))
pickle.dump(func,open('func.pkl','wb'))