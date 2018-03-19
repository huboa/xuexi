from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import redirect
from app01.forms import LoginForm
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


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login.html',{'form':form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            # form.cleaned_data#{"username":"alex",'password':'xxxx'}
            form.cleaned_data['password'] = md5(form.cleaned_data['password'])
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

from utils.pager import Pagination
def host(request):
    ##创建主机
    # for i in range(302):
    #     dic ={'hostname':'c%s.com' %(i,),"ip":'1.1.1.1','port':80}
    #     models.Host.objects.create(**dic)
    #
    # # return render(request,'host.html')
    # return HttpResponse("创建成功")


    all_count = models.Host.objects.all().order_by('-id').count()
    per_page_count = request.GET.get('items')
    if not per_page_count:
        per_page_count = 20
        print("check per_page_count ", per_page_count)
    else:
        per_page_count = int(per_page_count)
        print(per_page_count,type(per_page_count))
    # page_obj = Pagination(request.GET.get('page'),all_count,'/host/')
    page_obj = Pagination(all_count,per_page_count,request.GET.get('page'),request_url=request.path_info)
    host_list = models.Host.objects.all().order_by('-id')[page_obj.current_page_start_item:page_obj.current_page_end_item]
    return render(request, 'host.html', {'host_list': host_list, 'page_html': page_obj.page_html})
