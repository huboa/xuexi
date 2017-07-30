# -*- coding:utf-8 -*-
dic = {
    "河北": {
        "石家庄": {"鹿泉":{}, "藁城":{}, "元氏":{}},
        "邯郸": {"永年":{}, "涉县":{}, "磁县":{}},
    },
    "河南": {

    },
    "山西": {

    }}
now_menu = dic
prev_menu = []
while True:
    for key in now_menu:
        print(key)
    choice = input('>>').strip()
    if len(choice) == 0:continue
    if choice == 'q':exit()
    if choice == 'b':
        if len(prev_menu) > 0:
            now_menu = prev_menu.pop()
    if choice in now_menu:
        prev_menu.append(now_menu)
        now_menu = now_menu[choice]
