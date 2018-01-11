import time
from django.shortcuts import render,HttpResponse
from django.views.decorators.cache import cache_page

from rbac import models

from rbac.service.init_permissions import init_permission


def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
<<<<<<< HEAD
        print(user,pwd)
=======
>>>>>>> 895ccca56cdb4136ea39437e4c5c399b441561cd

        user = models.UserInfo.objects.filter(username=user,password=pwd).first()
        # user = models.UserInfo.objects.filter(username=user, password=pwd).all()
        print(user)
        if user:
            # 登录成功
<<<<<<< HEAD
            print('登录成功',user ,type(user))
            # role_list = user.roles.all()
            # print("rolelist",type(role_list),role_list)

            init_permission(user,request)

            return HttpResponse('welcome')
=======
            print('登录成功',user)
            # permission_list = user.roles.filter(permissions__id__isnull=False)
            permission_list = user.roles.filter(permissions__id__isnull=False).values(
                'permissions__title',
                'permissions__url',
                'permissions__code',
                'permissions__group_id',
            ).distinct()

            for permission in permission_list:
                print(permission)
            # """
            # {
            #     1: {
            #         urls: [/users/,/users/add/ ,/users/del/(\d+)/],
            #         codes: [list,add,del]
            #     },
            #     2: {
            #         urls: [/hosts/,/hosts/add/ ,/hosts/del/(\d+)/],
            #         codes: [list,add,del]
            #     }
            # }
            # """

            #permission[permissions__group_id]
            return HttpResponse('....')
>>>>>>> 895ccca56cdb4136ea39437e4c5c399b441561cd
        else:
            return render(request, 'login.html')

def user(request):
    user_list=models.UserInfo.objects.all()

    return render(request,"users.html",{'user_list':user_list})




#
#
# # @cache_page(60 * 15)
# def users(request):
#     # 写日志
#     # models.UserInfo.objects.create(username='alex')
#     # return HttpResponse('...')
#     ctime = str(time.time())
#     # return HttpResponse(ctime)
#     return render(request,'users.html',{'ctime':ctime})
#
#
# def multi_import(request):
#     # 写日志
#     models.UserInfo.objects.create(username='alex')
#     return HttpResponse('...')
