menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },

        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },

    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },

    '山东':{},
}

level=menu
llevel=[]
while True:
    for key in level:              ##打印列表
        print(key)
    choice = input(">>:").strip()   ##打印列表
    if len(choice) == 0: continue     ###检测输入
    if choice == "b":               ###返回判断
        if len(llevel) == 0:break   ##到第一层后退出
        level = llevel[-1]          ##标记位下层
        llevel.pop()                ##标记上层级
    if choice == "q":break          ##退出判断
    if choice not in level:continue  ###判断输入是否在列表里面
    llevel.append(level)              ##标记上层级
    level=level[choice]              ##标记下层级
