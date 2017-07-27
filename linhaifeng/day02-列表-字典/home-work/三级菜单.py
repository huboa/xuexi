#coding utf-8
dic = {
    "河北": {
        "石家庄": ["鹿泉", "藁城", "元氏"],
        "邯郸": ["永年", "涉县", "磁县"],
    },
    "河南": {
        "郑州": ["郑州1", "郑州2", "郑州3"],
        "安阳": ["安阳1", "安阳2", "安阳3"],
    },
    "山西": {
        "太原": ["太原1", "太原2", "太原3"],
        "大同": ["大同1", "大同2", "大同3"],
    }
}
x=[]
for province in dic:
    # print(province)
    x.append(province)
    for city in dic[province]:
        # print('----%s' %city)
        x.append(city)
        for county in dic[province][city]:
            # print('--------%s' %county)
            x.append(county)
#print(x)
while True:
    choice=input('请选择：').strip()
    if len(choice) != 0 and choice in x:
        for province in dic:
            if choice == province:
                for city in dic[province]:
                    print('----%s' % city)
            else:
                for city in dic[province]:
                   if choice == city:
                       for county in dic[province][city]:
                           print('--------%s' % county)


