
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

    print('level====', type(level),len(level))
    if key == "q" :
        exit()
    if isinstance(level,dict):  ###如果是字典则进入不是则不进入
        level=level[key]



    #     for key2 in dic[key1]:
    #         print(key2)