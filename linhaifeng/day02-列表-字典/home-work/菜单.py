
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

print(level["河北"])
# while True:
#     for n in level:
#         print(n)
#     key = input(" 请输入 >> :").strip()
#
#     print('level====', type(level))
#     level=dic[key]


    #     for key2 in dic[key1]:
    #         print(key2)