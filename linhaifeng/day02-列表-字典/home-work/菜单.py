
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
    for n in dic[key]:
        print(n)
    #     for key2 in dic[key1]:
    #         print(key2)