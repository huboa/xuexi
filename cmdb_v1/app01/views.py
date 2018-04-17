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
                return redirect('/user/')
            else:
                form.add_error("password","用户名或密码错误")

        return render(request,'login.html',{'form':form})


def index(request):
    return render(request,'index.html')

from utils.pager import Pagination
def host(request):
    ##创建主机测试数据
    # for i in range(302):
    #
    #     dic ={"idc":"廊坊","sn":"v%sasdfadf" %(i,),"remoteip":"1.1.1.1",'hostname':'c%s.com' %(i,),"ip":'1.1.1.1'}
    #     models.Host.objects.create(**dic)
    # return HttpResponse("创建成功")

    print(request.permission_codes)
    page_obj = Pagination(request,models.Host)

    return render(request, 'host.html', {'host_list': page_obj.obj_list_html, 'page_html': page_obj.page_html})
    # return render(request,'host.html', {'host_list': page_obj.obj_list_html,})
def add_host(request):
    if request.method == "GET":
        form = HostModelForm()
        # return render(request,"add_host.html",{'form':form})
        return render(request, "add_host.html", {'form': form})
    else:
        form =HostModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("/host/")
        return render(request, "add_host.html", {'form': form})

def edit_host(request,nid):

    obj = models.Host.objects.filter(id=nid).first()
    if not obj:
        return HttpResponse('数据不存在')
    if request.method == "GET":
        form = HostModelForm(instance=obj)
        return  render(request,'edit_host.html',{"form":form})
    else:
        form = HostModelForm(data=request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/host/')
        return render(request, 'edit_host.html', {'form': form})

def del_host(request,nid):
    obj = models.Host.objects.filter(id=nid).first()
    if not obj:
        return HttpResponse('数据不存在')
    else:
        models.Host.objects.filter(id=nid).delete()
        return redirect('/host/')