
dic = {
    "河北": {
        "石家庄": ["鹿泉", "藁城", "元氏"],
        "邯郸": ["永年", "涉县", "磁县"],
    },
    "河南": {
        ...
    },
    "山西": {
        ...
    }}
print(dic)

while True:
    key = input(">> :").strip()
    print(key)
    for key1 in dic:
         print(dic[key1])
    #     for key2 in dic[key1]:
    #         print(key2)