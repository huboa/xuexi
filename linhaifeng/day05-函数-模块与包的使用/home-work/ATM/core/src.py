from conf import settings
def search():
    print('search',settings.x)

def run():
    print('''
    1 查询
    2 购物
    3 转账
    ''')
    while True:
        choice=input('>>: ').strip()
        if not choice:continue
        if choice == '1':
            search()
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        else:
            pass
