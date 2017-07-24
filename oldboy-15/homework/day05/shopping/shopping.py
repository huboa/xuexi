
import os
import sys


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_dir)

#from atm.core import auth
# from core import main
from atm.core import login
#from atm.db   import DBOpt

@login.user_auth
def shopping():
    products =[["Mac",15800,1],["Ipone",5800,1],["bike",2000,1],["Coffee",30,1]]

    shopping_list=[]
    salary = input("input you salary >>:")
    salary = int(salary)


    while True:
        print("product list".center(20,"="))
        for index,i in enumerate(products):
            print(index,i[0],i[1])
        choice = input("请输入商品编号[quit]>>:")

        if choice.isdigit():
            choice=int(choice)
            if choice >= 0 and choice < len(products):
                #判断钱够不够
                p=products[choice]
                if salary >= p[1]:
                    salary -= p[1]
                    shopping_list.append(p)##加入购物车
                    print("[%s] 已加入购物车,您还可以购买[%s]元的商品" %(p[0],salary))
                    print("您的购物车")
                    for j,k in enumerate(shopping_list):
                        j+=1
                        print(j,k[0],k[1])
                else:
                    print(salary)
                    print("你的余额[%s]不足"%salary)
            else:
                print("没有此商品...")
        elif choice == "quit":
            print("已购买商品".center(20,"="))
            for i,j in enumerate(shopping_list):
                i+=1

                print(i,j[0],j[1])
            print("余额",salary)
            exit()

shopping