from django.shortcuts import render,redirect,HttpResponse
from app01.forms import LoginForm
from app01 import models
from django.conf import settings# 仅用户自定义+内置
# from s18day24 import settings    # 仅用户自定义
from utils.md5 import md5




def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request,'login.html',{'form':form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            # form.cleaned_data # {'username':'alex','password':'xxxx'}
            # models.UserInfo.objects.filter(username=form.cleaned_data['user'],password=form.cleaned_data['pwd'])
            # models.UserInfo.objects.filter(**{'username':'alex','password':123})
            form.cleaned_data['password'] = md5(form.cleaned_data['password'])
            user = models.UserInfo.objects.filter(**form.cleaned_data).first()
            if user:
                # 将用户信息放置到session中
                request.session[settings.USER_SESSION_KEY] = {'id':user.pk,'username':user.username }
                return redirect('/index/')
            else:
                form.add_error('password', '用户名或密码错误')
        return render(request, 'login.html',{'form':form})


def index(request):
    return HttpResponse('欢迎登陆')









