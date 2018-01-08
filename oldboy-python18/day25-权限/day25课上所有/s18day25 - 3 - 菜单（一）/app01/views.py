import time
from django.shortcuts import render,HttpResponse
from django.views.decorators.cache import cache_page

from rbac import models
from rbac.service.init_permission import init_permission

def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user = models.UserInfo.objects.filter(username=user,password=pwd).first()
        if user:
            # 登录成功
            init_permission(user,request)
            return HttpResponse('登录成功')
        else:
            return render(request, 'login.html')


def users(request):
    print(request.permission_codes)
    user_list = models.UserInfo.objects.all()
    return render(request,'users.html',{'user_list':user_list})


def users_add(request):
    return HttpResponse('添加页面')









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
