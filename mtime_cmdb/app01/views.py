from django.shortcuts import render
from django.shortcuts import redirect
from app01.forms import LoginForm
from  app01 import models
from django.conf import settings
from utils.md5 import  md5
# Create your views here.

def login(request):
    if request.method == 'GET':
        form =LoginForm()
        return render(request,'login.html',{'form':form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            # form.cleaned_data#{"username":"alex",'password':'xxxx'}
            print(form.cleaned_data)
            # form.cleaned_data['password'] = md5(form.cleaned_data['password'])
            user=models.UserInfo.objects.filter(**form.cleaned_data).first()
            print(user,"user")
            if user:
                ###将用户信息方session
                 request.session[settings.USER_SESSION_KEY] ={'id':user.pk,'username':user.username}
                 return redirect('/index/')
            else:
                form.add_error("password","用户名或密码错误")

        return render(request,'login.html',{'form':form})
def index(request):
    return render(request,'index.html')
