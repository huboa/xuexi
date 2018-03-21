from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings  # 仅用户自定义+内置
# from root import settings    # 仅用户自定义
from app01.forms import LoginForm,HostModelForm
from app01 import models
from utils.md5 import md5
from django.utils.safestring import mark_safe


def auth(func):
    def inner(request, *args, **kwargs):
        # 在执行视图函数之前
        user_info = request.session.get(settings.USER_SESSION_KEY)
        if not user_info:
            return redirect('/login/')
        # 执行视图函数
        response = func(request, *args, **kwargs)
        return response

    return inner


def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            # form.cleaned_data # {'username':'alex','password':'xxxx'}
            # models.UserInfo.objects.filter(username=form.cleaned_data['user'],password=form.cleaned_data['pwd'])
            # models.UserInfo.objects.filter(**{'username':'alex','password':123})
            form.cleaned_data['password'] = md5(form.cleaned_data['password'])
            print(form.cleaned_data)
            user = models.UserInfo.objects.filter(**form.cleaned_data).first()
            if user:
                # 将用户信息放置到session中
                request.session[settings.USER_SESSION_KEY] = {'id': user.pk, 'username': user.username}
                return redirect('/index/')
            else:
                form.add_error('password', '用户名或密码错误')
        return render(request, 'login.html', {'form': form})


def index(request):
    return render(request,'index.html')


def test(request):
    # 序列化一：
    # from django.core import serializers
    # host_list = models.Host.objects.filter(id__lt=5)
    # data = serializers.serialize("json", host_list)

    # 序列化二：
    import json
    host_list = models.Host.objects.filter(id__lt=5).values('id','hostname','port','ctime')
    data = json.dumps(list(host_list))
    return HttpResponse(data)

from utils.pager import Pagination
def host(request):
    all_count = models.Host.objects.all().order_by('-id').count()
    # page_obj = Pagination(request.GET.get('page'),all_count,'/host/')
    page_obj = Pagination(request.GET.get('page'),all_count,request.path_info)
    host_list = models.Host.objects.all().order_by('-id')[page_obj.start:page_obj.end]
    return render(request,'host.html',{'host_list':host_list,'page_html':  page_obj.page_html()})


def add_host(request):
    if request.method == "GET":
        form = HostModelForm()
        return render(request,'add_host.html',{'form':form})
    else:
        form = HostModelForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            obj = form.save()
            return redirect('/host/')
        return render(request, 'add_host.html', {'form': form})


def edit_host(request,eid):
    print(request,eid)
    obj = models.Host.objects.filter(id=eid).first()

    if not obj:
        return HttpResponse('数据不存在')

    if request.method == "GET":
        form = HostModelForm(instance=obj)
        return render(request,'edit_host.html',{'form':form})
    else:
        form = HostModelForm(data=request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/host/')
        return render(request, 'edit_host.html', {'form': form})



