
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

    key = input("请输入: q退出 m主菜单  -->> :").strip()

    if key == ""  :continue
    if key == "q" :exit()   ##退出

    if key == "m" :   ###回退主菜单
        level=dic
        continue

    if key in level:  ##判断在不在里面
        level = level[key]
    else:
        print("请输入正确选项")


    if isinstance(level,list):  ###如果是字典则进入不是则不进入
        print("已经是最后一层")
        continue



