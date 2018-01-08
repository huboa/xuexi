from django.conf import settings

def init_permission(user,request):
    """
    用于做用户登录成功之后，权限信息的初始化。
    :param user: 登录的用户对象
    :param request: 请求相关的对象
    :return:
    """


    """
                [
                    {'permissions__title': '用户列表', 'permissions__url': '/users/', 'permissions__code': 'list', 'permissions__group_id': 1}
                    {'permissions__title': '添加用户', 'permissions__url': '/users/add/', 'permissions__code': 'add', 'permissions__group_id': 1}
                    {'permissions__title': '删除用户', 'permissions__url': '/users/del/(\\d+)/', 'permissions__code': 'del', 'permissions__group_id': 1}
                    {'permissions__title': '修改用户', 'permissions__url': '/users/edit/(\\d+)/', 'permissions__code': 'edit', 'permissions__group_id': 1}
                    {'permissions__title': '主机列表', 'permissions__url': '/hosts/', 'permissions__code': 'list', 'permissions__group_id': 2}
                    {'permissions__title': '添加主机', 'permissions__url': '/hosts/add/', 'permissions__code': 'add', 'permissions__group_id': 2}
                    {'permissions__title': '删除主机', 'permissions__url': '/hosts/del/(\\d+)/', 'permissions__code': 'del', 'permissions__group_id': 2}
                    {'permissions__title': '修改主机', 'permissions__url': '/hosts/edit/(\\d+)/', 'permissions__code': 'edit', 'permissions__group_id': 2}
                ]

                {
                    1(权限组ID): {
                        urls: [/u sers/,/users/add/ ,/users/del/(\d+)/],
                        codes: [list,add,del]
                    },
                    2: {
                        urls: [/hosts/,/hosts/add/ ,/hosts/del/(\d+)/],
                        codes: [list,add,del]
                    }
                }

                """
    permission_list = user.roles.filter(permissions__id__isnull=False).values(
        'permissions__title',
        'permissions__url',
        'permissions__code',
        'permissions__group_id',
    ).distinct()

    permission_dict = {}
    """
    {
        1: {
            urls: ['/users/', ],
            codes: ['list',]
        }
    }

    """
    for permission in permission_list:
        group_id = permission['permissions__group_id']
        url = permission['permissions__url']
        code = permission['permissions__code']
        if group_id in permission_dict:
            permission_dict[group_id]['urls'].append(url)
            permission_dict[group_id]['codes'].append(code)
        else:
            permission_dict[group_id] = {'urls': [url, ], 'codes': [code, ]}

    request.session[settings.PERMISSION_DICT_SESSION_KEY] = permission_dict




