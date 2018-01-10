from django.conf import settings

def init_permission(user,request):

    '''
    用于做用户登录成功后,权限信息初始化
    :param user:登陆用户对象
    :param request:请求相关对象
    :return:
    '''


    # title_list = user.roles.all().values("id","title","permissions__title")
    # print("title_list",type(title_list),title_list)

    # permission_list_test = user.roles.all().values("permissions__title",'permissions__url','permissions__code','permissions__groupid',)
    # print(permission_list_test)

    permission_list = user.roles.filter(permissions__id__isnull=False).values(
        'permissions__title',
        'permissions__url',
        'permissions__code',
        'permissions__group_id',
    ).distinct()

    permission_dic = {}
    for permission in permission_list:
        """
    {
        1: {
            urls: [/users/,/users/add/ ,/users/del/(\d+)/],
            codes: [list,add,del]
        },
        2: {
            urls: [/hosts/,/hosts/add/ ,/hosts/del/(\d+)/],
            codes: [list,add,del]
        }
    }
    """
        print(permission)
        dict_id = permission["permissions__group_id"]
        dict_title = permission["permissions__title"]
        dict_url = permission["permissions__url"]
        dict_code = permission["permissions__code"]

        ##按组创建字典
        if dict_id not in permission_dic:
            permission_dic[dict_id] = {'urls': [], 'codes': []}
        ##追加数据
        permission_dic[dict_id]["urls"].append(dict_url)
        permission_dic[dict_id]["codes"].append(dict_code)

    print(permission_dic)

    request.session[settings.PERMISSIONS_DICT_SESSION_KEY] = permission_dic