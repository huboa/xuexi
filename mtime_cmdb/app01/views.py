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

def host(request):
    ##创建主机
    # for i in range(302):
    #     dic ={'hostname':'c%s.com' %(i,),"ip":'1.1.1.1','port':80}
    #     models.Host.objects.create(**dic)
    #
    # # return render(request,'host.html')
    # return HttpResponse("创建成功")


    ##显示主机数
    all_item = models.Host.objects.all().order_by('-id').count()###总item数
    per_page_count = 10    ###每页显示多少item

    remainder_item = all_item % per_page_count
    if remainder_item == 0 :
        all_page = int(all_item // per_page_count)
    else:
        all_page = int(all_item // per_page_count + 1)


    print("主机数",all_item,"总页数",all_page,"最后一页",remainder_item)
    request_current_page = request.GET.get("page")     ##当前页

    if  request_current_page:
        current_page = int(request_current_page)
    else:
        current_page = 1

   ###每页显示主机数
    current_page_start_item=(current_page-1) * per_page_count  ###当前起始item

    if  current_page == all_page + 1:
        current_page_end_item = all_item

    else:
        current_page_end_item=current_page_start_item + per_page_count

    print("当前页码",current_page, current_page_start_item , current_page_end_item,"总页数",all_page, )
    host_list = models.Host.objects.all()[current_page_start_item:current_page_end_item]






    per_group_page = 10  ##显示页码数

    if all_page % per_group_page == 0:
        all_page_group = int(all_page//per_group_page) ##　#总的 页码组
    else:
        all_page_group = int(all_page // per_group_page + 1)

    ###页码所在组
    current_page_group_id = int((current_page-1)/per_group_page)
    current_page_group_start =current_page_group_id*per_group_page + 1

    if current_page_group_id == all_page_group - 1:
        current_page_group_end = current_page_group_id*per_group_page + all_page%per_group_page
        print("最后一组")
    else:
        current_page_group_end  =  current_page_group_start + per_group_page - 1
    print("当前页码组",current_page_group_id,current_page_group_start, current_page_group_end ,"总组数",all_page_group)

    page_html = ''
    for i in range(current_page_group_start, current_page_group_end + 1):
        if i == current_page:
            temp = '<a class="active" href="/host/?page=%s">%s</a>' % (i, i)
        else:
            temp = '<a href=/host/?page=%s>%s</a>' % (i, i,)
        page_html += temp


###前一页码
    if current_page > 1:
        pre_page = current_page - 1
        pre_page_html = '<a href=/host/?page=%s><</a>' % (pre_page)
    else:
        pre_page = current_page
        pre_page_html = '<a href=/host/?page=%s><</a>' % (pre_page)

    if current_page < all_page:
        next_page = current_page  + 1
        next_page_html = '<a href=/host/?page=%s>></a>' % (next_page )
    else:
        next_page = current_page
        next_page_html = '<a href=/host/?page=%s>></a>' % (next_page)
#
# ####前一组
#
#     if  current_page_step > 1:
#         pre_page_step = current_page - 10*per_page_count + 1
#         pre_page_step_html = '<a href=/host/?page=%s><<</a>' % (pre_page_step)
#     else:
#         pre_page_step = current_page
#         pre_page_step_html = '<a href=/host/?page=%s><</a>' % (pre_page_step)
#
#     if current_page_step > all_page_step:
#         next_page_step = current_page + 1
#         next_page_step_html = '<a href=/host/?page=%s>>></a>' % (next_page_step)
#     else:
#         next_page_step = current_page  +  10*per_page_count + 1
#         next_page_step_html = '<a href=/host/?page=%s>>></a>' % (next_page_step)
#
#     page_html = pre_page_step_html + pre_page_html + page_html + next_page_html + next_page_step_html
    page_html =   pre_page_html + page_html + next_page_html



    return render(request,'host.html',{'host_list':host_list,'page_html':page_html})
    # return render(request,'host.html',{'host_list':host_list})