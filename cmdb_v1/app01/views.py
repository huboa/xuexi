from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import redirect
from app01.forms import LoginForm,HostModelForm
from rbac.models import  UserInfo
from  app01 import models
from django.conf import settings
from utils.md5 import  md5
from rbac.service.init_permissions import init_permissions
from rbac.service.init_permissions import user_state
from rbac.service.init_permissions import reset_permission


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


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login.html',{'form':form})
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

                print('login sessinkiey',request.session.session_key)
                user.session_key=request.session.session_key
                print(request.session.session_key)
                print(request.session.keys())
                print(request.session.values())
                print(request.session.items())
                user.save()
                return redirect('/index/')
            else:
                form.add_error("password","用户名或密码错误")

        return render(request,'login.html',{'form':form})

def logout(request):
    session_key=request.session.session_key
    reset_permission(session_key,request)
    print("删除session",session_key)
    return redirect('/index/')

def index(request):
    request_host=(request.get_host())
    print("/index/",request.session.session_key)
    print(user_state(request))
    print(user_state(request),request_host)
    return render(request,'index.html',{'request_host':request_host,"login_state":user_state(request)})




