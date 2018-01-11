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

        print(user,pwd)
        user = models.UserInfo.objects.filter(username=user,password=pwd).first()
        # user = models.UserInfo.objects.filter(username=user, password=pwd).all()
        print(user)
        if user:
            # 登录成功

            print('登录成功',user ,type(user))
            # role_list = user.roles.all()
            # print("rolelist",type(role_list),role_list)

            init_permission(user,request)

            return HttpResponse('welcome')

        else:
            return render(request, 'login.html')

def users(request):
    users_list=models.UserInfo.objects.all()

    return render(request,"users.html",{'users_list':users_list})




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
