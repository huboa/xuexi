
dic = {
    "河北": {
        "衡水": ["安平", "饶阳", "神州"],
        "石家庄": ["鹿泉", "藁城", "元氏"],
        "邯郸": ["永年", "涉县", "磁县"],
    },
    "河南": {
        ...
    },
    "山西": {
        ...
    }}

level=dic

while True:
    for n in level:  ##显示字典
        print(n)

    key = input("请输入: q退出 m主菜单  -->> :").strip()

    if key == ""  :continue
    if key == "q" :exit()   ##退出

    if key == "m" :   ###回退主菜单
        level=dic
        continue



    if key in level:  ##判断在不在里面
        if not isinstance(level, dict): continue  ##判断是不是字典
        level = level[key]
    else:
        print("请输入正确选项")

