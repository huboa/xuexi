'''二、用户交互，显示省市县三级联动的选择
要求：用户输入河北，则打印河北省下的市，用户输入市，则显示该河北省的这个市下的县'''
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
},
}
while True:
    for i in dic:
        print(i)
    shengcheng = input('请输入省[q退出]： ').strip()
    if shengcheng == 'q':
        exit()
    elif shengcheng in dic:
        while True:
            for i2 in dic[shengcheng]:
                print(i2)
            shixian = input('请输入市[q返回上一层] ： ').strip()
            if shixian in dic[shengcheng]:
                while True:
                    for i3 in dic[shengcheng][shixian]:
                        print(i3)
                    fh = input('只有这些了,输入q返回上一层： ')
                    if fh == 'q':
                        break
                    else:
                            print('请重新输入！')
            elif shixian == 'q':
                break
            else:
                print('请重新输入！')
    else:
        print('请重新输入！')

