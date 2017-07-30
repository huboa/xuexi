
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

level=dic


while True:
    for n in level:
        print(n)
    key = input(" 请输入 >> :").strip()


    level=dic[key]
    print('level',type(level))

    #     for key2 in dic[key1]:
    #         print(key2)