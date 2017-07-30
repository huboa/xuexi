
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

back_level=[]
while True:
    for n in level:
        print(n)
    key = input(" e：退出 m:主菜单，请输入  >> :").strip()

    if key == ""  :continue
    if key == "q" :exit()   ##退出
    if key == "m" :
        level=dic ###回退主菜单
        continue

    if isinstance(level,dict):  ###如果是字典则进入不是则不进入
        level=level[key]

        print("test",str(dict))