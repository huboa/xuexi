
# Create your tests here.
# from  rbac import models
#
# user =models.UserInfo.objects.get(username='root')
# print(user)

menu_list = [{'pid': 1, 'id': 1, 'url': '/user/', 'menu_id': 1, 'title': '用户列表 ', 'menu_name': '菜单'}, {'pid': 1, 'id': 2, 'url': '/user/add/', 'menu_id': 1, 'title': '添加用户', 'menu_name': '菜单'}, {'pid': 1, 'id': 3, 'url': '/user/del/(\\d+)/', 'menu_id': 1, 'title': '删除用户', 'menu_name': '菜单'}, {'pid': 1, 'id': 4, 'url': '/user/edit/(\\d+)/', 'menu_id': 1, 'title': '修改用户 ', 'menu_name': '菜单'}, {'pid': 5, 'id': 5, 'url': '/host/', 'menu_id': 1, 'title': '主机列表', 'menu_name': '菜单'}, {'pid': 5, 'id': 6, 'url': '/host/add/', 'menu_id': 1, 'title': '添加主机', 'menu_name': '菜单'}, {'pid': 5, 'id': 7, 'url': '/host/del/(\\d+)/', 'menu_id': 1, 'title': '删除主机', 'menu_name': '菜单'}, {'pid': 5, 'id': 8, 'url': '/host/edit/(\\d+)/', 'menu_id': 1, 'title': '修改主机', 'menu_name': '菜单'}, {'pid': 9, 'id': 9, 'url': '/role/', 'menu_id': 1, 'title': '角色列表', 'menu_name': '菜单'}, {'pid': 9, 'id': 10, 'url': '/role/add/', 'menu_id': 1, 'title': '添加角色', 'menu_name': '菜单'}, {'pid': 9, 'id': 11, 'url': '/role/del/(\\d+)/', 'menu_id': 1, 'title': '删除角色', 'menu_name': '菜单'}, {'pid': 9, 'id': 12, 'url': '/role/edit/(\\d+)/', 'menu_id': 1, 'title': '编辑角色', 'menu_name': '菜单'}, {'pid': 13, 'id': 13, 'url': '/permission/', 'menu_id': 1, 'title': '权限列表', 'menu_name': '菜单'}, {'pid': 13, 'id': 14, 'url': '/permission/add/', 'menu_id': 1, 'title': '添加权限', 'menu_name': '菜单'}, {'pid': 13, 'id': 15, 'url': '/permission/del/(\\d+)/', 'menu_id': 1, 'title': '删除权限', 'menu_name': '菜单'}, {'pid': 13, 'id': 16, 'url': '/permission/edit/\\d(+)/', 'menu_id': 1, 'title': '编辑权限', 'menu_name': '菜单'}]

per_dict = {}

for item in menu_list:
    print(item)
    if item['id'] == item['pid']:
        per_dict[item['id']] = item
print(per_dict)
for n in per_dict.values():
    print(n)