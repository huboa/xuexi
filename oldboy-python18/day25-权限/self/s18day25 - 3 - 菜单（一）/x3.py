
menu_list={
    1: {'id': 1, 'title': '用户列表', 'url': '/users/', 'pid': None, 'menu_id': 1, 'menu__name': '菜单1', 'active': True},
    5: {'id': 5, 'title': '主机列表', 'url': '/hosts/', 'pid': None, 'menu_id': 1, 'menu__name': '菜单1'},
    10: {'id': 10, 'title': 'xx列表', 'url': '/hosts/', 'pid': None, 'menu_id': 2, 'menu__name': '菜单2'}
}

{
    1: {
        'menu__name': '菜单1',
        'active': True,
        'children': [
            {'id': 1, 'title': '用户列表', 'url': '/users/', 'active': True}
            {'id': 5, 'title': '主机列表', 'url': '/users/'}
        ]
    },
    2: {
        'menu__name': '菜单1',
        'children': [
            {'id': 10, 'title': 'xx列表', 'url': '/hosts/'}
        ]

    }
}

menu_list=[]
print(menu_list)