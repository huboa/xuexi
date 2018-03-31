from  rbac.models import UserInfo
from django.conf import settings
from django.shortcuts import render,HttpResponse

def init_permissions(user):

    #把权限列表转换成字典格式
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
    # permission_list = UserInfo.roles.all(permissions__id__isnull=False).values(
    #     'permissions__title',
    #     'permissions__url',
    #     'permissions__code',
    #     'permissions__group_id',
    # ).distinct()
    # permission_list = UserInfo.roles.all()


    #
    #         """           pass
    #
    #
    #
    #             {
    #                 1: {
    #                     urls: ['/users/', ],
    #                     codes: ['list',]
    #                 }
    #             }
    #         '''
    #

    permission_list = UserInfo.objects.get(username=user).roles.all().values('permisions__id',
                                                                             'permisions__url',
                                                                             'permisions__code',
                                                                             'permisions__code',
                                                                               'permisions__group_id',
                                                                             ).distinct()

    # print(t,"$$$$$$ttttttt$$$$$",type(t))
    # permission_list = t.roles.all().values('permisions__id','permisions__url','permisions__code','permisions__code','permisions__group_id')


    # print("permission",type(permission_list),permission_list)
    permission_dict = {}
    for permission in permission_list:
        group_id = permission["permisions__group_id"]
        url = permission["permisions__url"]
        code = permission["permisions__code"]
        if group_id in permission_dict:
            permission_dict[group_id]['url'].append(url)
            permission_dict[group_id]['code'].append(code)

        else:
            permission_dict[group_id] = {'url': [], 'code': []}
            permission_dict[group_id]['url'].append(url)
            permission_dict[group_id]['code'].append(code)

    return permission_dict