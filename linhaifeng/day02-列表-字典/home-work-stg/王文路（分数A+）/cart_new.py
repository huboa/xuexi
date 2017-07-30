# -*- coding:utf-8 -*-
import os
import datetime
# 初始化登录用户信息
user_login = {}
# 查询用户信息
def usersinfo():
    with open('db.txt','r',encoding='utf-8') as f:
        return dict(eval(f.read()))
# 用户登录输入
def login_input():
    user = input('用户名：').strip()
    passwd = input('密码：').strip()
    return user,passwd
# 登录验证
def login_verify():
    count = 0
    while count < 3:
        user_input = login_input()
        username = user_input[0]
        password = user_input[1]
        users = usersinfo()
        if username in users:
            if password == users[username]['password']:
                user_login['name'] = username
                return 'True'
            else:
                count += 1
                print('密码错误')
        else:
            count += 1
            print('用户不存在')
    else:
        return '登陆次数过于频繁'
# 商品信息
def goodsinfo():
    with open('goods.txt','r',encoding='utf-8') as g:
        return list(eval(g.read()))
# 用户信息更改操作
def write(info):
    with open('db_new.txt','w',encoding='utf8') as w:
        w.write(info)
    os.remove('db.txt')
    os.rename('db_new.txt','db.txt')
# 登录系统显示样式
def welcome():
    print(''.center(50, '*'))
    print('*', ''.center(46, ' '), '*')
    print('*', '欢迎来到购物广场'.center(38, ' '), '*')
    print('*', ''.center(46, ' '), '*')
    print(''.center(50, '*'))
    print('s:选购商品  r:充值  c:购物车  a:结算  q:exit')
    print('登录信息：')
    print(''.center(50, '*'))
    print('用户名：\033[31;1m%s\033[1m \t余额：\033[34;1m%s\033[1m' % (user_login['name'],usersinfo()[user_login['name']]['balance']))
    print(''.center(50, '*'))
# 商品展示
def goods_show():
    # print(goodsinfo())
    print('商品列表'.center(46,'*'))
    print('%10s%10s%10s' % ('编号','商品名称','商品价格'))
    for key,goods in enumerate(goodsinfo()):
        print('%10s\t%10s\t%10s' % (key, goods['name'], goods['price']))
    print(''.center(50, '*'))
# 购物车展示
def cart_show():
    print('购物车'.center(46,'*'))
    print('%10s%10s%10s' % ('名称', '价格','数量'))
    cart = usersinfo()[user_login['name']]['cart']
    for goods in cart:
        print('%10s\t%10s\t%10s' % (goods, cart[goods][0],cart[goods][1]))
    print(''.center(50, '*'))
# 购物操作
def go_shoping():
    print('已进入购物模式[q:退出]')
    while True:
        goods_show()
        goods_choice = input('请选择物品编号购买[q:退出]：').strip()
        if goods_choice == 'q':
            break
        if goods_choice.isdigit():
            goods_choice = int(goods_choice)
        else:
            print('输入格式有误，请重新选择')
            continue
        if goods_choice in list(range(len(goodsinfo()))):
            users = usersinfo()
            choice = goodsinfo()[goods_choice] # 用户本次加入购物车的商品信息
            cart = users[user_login['name']]['cart'] # 用户购物车'cart': {'name': ['price', 'num'], 'name2': ['price2', 'num2']}}

            if choice['name'] in cart:
                users[user_login['name']]['cart'][choice['name']] = [choice['price'],(int(cart[choice['name']][1])+1)]
            else:
                users[user_login['name']]['cart'][choice['name']] = [choice['price'],1]
            write(str(users))
            print('add \033[32;1m%s\033[1m to cart' % choice['name'])
        else:
            print('\033[31;1m所选商品不存在\033[1m')
# 充值操作
def balance_recharge():
    print('已进入充值模式[q:退出]')
    users = usersinfo()
    print('您当前账户余额为：\033[34;1m%s\033[1m' % users[user_login['name']]['balance'])
    sign = True
    while sign:
        money = input('请输入要充值金额[q:退出]：').strip()
        if money == 'q':
            break
        if money.isdigit():
            money = int(money)
        else:
            print('\033[31;1m充值金额应为数字\033[1m')
            continue
        if money <= 0:
            print('\033[31;1m充值金额应大于0\033[1m')
            continue
        while True:
            flag = input('是否充值？[y/n]').strip()
            if flag.lower() == 'y':
                users[user_login['name']]['balance'] = int(users[user_login['name']]['balance']) + money
                write(str(users))
                print('\033[32;1m充值成功\033[1m,账户余额为：\033[34;1m%s\033[1m' % usersinfo()[user_login['name']]['balance'])
                break
            elif flag.lower() == 'n':
                sign = False
                break
            else:
                print('\033[31;1m输入格式错误\033[1m')
# 购物车管理
def cart_manager():
    print('已进入购物车模式[q:退出]')
    users = usersinfo()
    cart = users[user_login['name']]['cart']
    while True:
        cart_show()
        cart_name = input('请选择要修改的商品名称[q:退出]：').strip()
        if cart_name == 'q':
            break
        if cart_name in cart:
            print('名称：\033[34;1m%s\033[1m 数量：\033[34;1m%s\033[1m' % (cart_name, cart[cart_name][1]))
            operate = input('请选择[d:删除 u:修改数量 q:退出]：').strip()
            if operate.lower() == 'd':
                confir = input('确认删除？y/n:').strip()
                if confir.lower() == 'y':
                    users[user_login['name']]['cart'].pop(cart_name)
                    write(str(users))
                    print('\033[32;1m[%s]已删除\033[1m' % cart_name)
                    continue
                elif confir.lower() == 'n':
                    continue
                else:
                    print('\033[31;1m输入错误\033[1m')
            elif operate.lower() == 'u':
                while True:
                    num = input('输入要修改数量[b:返回]：').strip()
                    if num == 'b':
                        break
                    if num.isdigit():
                        num = int(num)
                    else:
                        print('\033[31;1m输入格式错误\033[1m')
                        continue
                    if num <= 0:
                        print('\033[31;1m商品数量应大于0\033[1m')
                        continue
                    if num == int(cart[cart_name][1]):
                        print('\033[32;1m修改成功\033[1m')
                        break
                    users[user_login['name']]['cart'][cart_name][1] = num
                    confirm = input('确认修改？y/n：').strip()
                    if confirm.lower() == 'y':
                        write(str(users))
                        print('\033[32;1m修改成功\033[1m')
                        break
                    elif confirm.lower() == 'n':
                        break
                    else:
                        print('\033[31;1m输入错误\033[1m')
            elif operate.lower() == 'q':
                continue
            else:
                print('\033[31;1m输入错误\033[1m')
        else:
            print('\033[31;1m商品不存在\033[1m')
# 购物车总费用
def cart_fee():
    users = usersinfo()
    cart = users[user_login['name']]['cart']
    sum = 0
    for key in cart:
        sum += (int(cart[key][0]) * int(cart[key][1]))
    return sum
# 购买成功写入日志
def write_log():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cart = usersinfo()[user_login['name']]['cart']
    item = []
    item.append(now)
    item.append(user_login['name'])
    for k,key in enumerate(cart):
        item.append('商品名：%s 商品数量：%s 小计：%s' % (key,cart[key][1],(int(cart[key][0])*int(cart[key][1]))))
    item.append(' 总计：%s \n' % cart_fee())
    item = ' '.join(item)
    with open('record.log','a',encoding='utf-8') as f:
        f.write(item)
# 结算操作
def settlement():
    print('已进入结算模式[q:退出]')
    users = usersinfo()
    amount = int(cart_fee())
    if amount > int(users[user_login['name']]['balance']):
        print('\033[31;1m余额不足,充值金额应大于 %s\033[1m' % (amount-int(users[user_login['name']]['balance'])))
        while True:
            mode = input('请选择[r:充值 c:购物车 q:退出]：').strip()
            if mode.lower() == 'r':
                balance_recharge()
            elif mode.lower() == 'c':
                cart_manager()
            elif mode.lower() == 'q':
                break
            else:
                print('\033[31;1m输入错误\033[1m')
                continue
    else:
        cart_show()
        while True:
            confirm = input('确认购买？y/n:').strip()
            if confirm.lower() == 'y':
                users[user_login['name']]['cart'] = {}
                users[user_login['name']]['balance'] = int(users[user_login['name']]['balance']) - amount
                write_log()
                write(str(users))
                print('\033[32;1m购买成功\033[1m')
                break
            elif confirm.lower() == 'n':
                break
            else:
                print('\033[31;1m输入错误\033[1m')
# 主函数
def main():
    print('请登录后进入购物广场')
    login_status = login_verify()
    if login_status == 'True':
        welcome()
        while True:
            user_choice = input('请选择模式[s:选购商品  r:充值  c:购物车  a:结算  q:exit]：').strip()
            if user_choice == 's':
                go_shoping()
            elif user_choice == 'r':
                balance_recharge()
            elif user_choice == 'c':
                cart_manager()
            elif user_choice == 'a':
                settlement()
            elif user_choice == 'q':
                print('\033[31;1m拜拜！\033[1m')
                break
            else:
                print('[warning]输入错误')
    else:
        print(login_status)
if __name__ == '__main__':
    main()
