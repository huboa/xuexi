
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
back_level=dic
while True:
    for n in level:
        print(n)
    key = input(" 请输入 >> :").strip()

    print('level====', type(level),len(level))
    if key == ""  :continue
    if key == "q" :exit()   ##退出
    if key == "b" :
        level=back_level  ###回退前一列表
        print(back_level)
        continue

    if isinstance(level,dict):  ###如果是字典则进入不是则不进入
        back_level=level
        level=level[key]



    #     for key2 in dic[key1]:
    #         print(key2)