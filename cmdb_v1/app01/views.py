from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import redirect
from app01.forms import LoginForm,HostModelForm
from rbac.models import  UserInfo
from  app01 import models
from django.conf import settings
from utils.md5 import  md5


# Create your views here.

###装饰圈
# def auth(func):
#     def inner(request,*args,**kwargs):
#         user_info = request.session.get(settings.USER_SESSION_KEY)
#         if not user_info:
#             return redirect('/login')
#         response = func(request,*args,**kwargs)
#         return response
#     return inner
#

from rbac.service.init_permissions import init_permissions
def login(request):
    request_host = (request.get_host())
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login.html',{'form':form,'request_host':request_host})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            # form.cleaned_data#{"username":"alex",'password':'xxxx'}
            form.cleaned_data['password'] = md5(form.cleaned_data['password'])
            # user=models.UserInfo.objects.filter(**form.cleaned_data).first()

            user = UserInfo.objects.filter(**form.cleaned_data).first()
            print(user,"user")
            if user:
                ###将用户信息方session
                init_permissions(user,request)
                return redirect('/index/')
            else:
                form.add_error("password","用户名或密码错误")

        return render(request,'login.html',{'form':form})


def index(request):
    request_host=(request.get_host())
    user_online_status=request.session.get(settings.PERMISSION_DICT_SESSION_KEY)

    return render(request,'index.html',{'request_host':request_host,"user_online_status":user_online_status})




