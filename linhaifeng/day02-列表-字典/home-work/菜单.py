
dic = {
    "河北": {
        "衡水": ["安平", "饶阳", "深州"],
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
    for n in level:  ##显示字典
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



