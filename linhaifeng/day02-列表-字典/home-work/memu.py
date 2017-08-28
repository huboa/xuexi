menu = {
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
level=[]
while True:
    for key in menu:
        print(key)
    choice=input("choie>>:").strip()
    if choice == 'b':
        if len(level) == 0 : break
        menu=level[-1]
        level.pop()

    if len(choice) == 0 or choice not in menu:continue
    if  type(menu) == list  :continue
    level.append(menu)
    menu=menu[choice]
