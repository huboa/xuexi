dic = {
    "河北": {
        "石家庄": ["鹿泉", "藁城", "元氏"],
        "邯郸": ["永年", "涉县", "磁县"],
        "邢台":["a","b","c"]
    },
    "江苏": {
        "连云港":["灌南","灌云","新浦"],
        "南京":["4","5","6"],
        "无锡":["1","2","3"]
    }
	}
name=input("请输入中国省名称：")
if name in dic:
    for i in dic[name].keys():
        print(i)
city = input("请输入城市名称：")
if city  in dic[name].keys():
    for c in (dic[name][city]):
        print(c)



