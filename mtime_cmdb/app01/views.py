from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import redirect
from app01.forms import LoginForm,HostModelForm
from  app01 import models
from  rbac.models import UserInfo
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
            # user=models.UserInfo.objects.filter(**form.cleaned_data).first()

            user = UserInfo.objects.filter(**form.cleaned_data).first()
            print(user,"user")
            if user:
                ###将用户信息方session
                # permissions_list = user.role.
                #  print(permissions_list, "###################")
                 request.session[settings.USER_SESSION_KEY] ={'id':user.pk,'username':user.username}
                 # permissions_list= user.role.fiter(permission__id__isnull=False).values().distinct()


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

def add_host(request):
    if request.method == "GET":
        form = HostModelForm()
        return render(request,"add_host.html",{'form':form})
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


def users(request):
    users = UserInfo.objects.filter(username="zsc")
    print(users,type(users),"#########")

    """
                [
                    {'permissions__title': '用户列表', 'permissions__url': '/users/', 'permissions__code': 'list', 'permissions__group_id': 1}
                    {'permissions__title': '添加用户', 'permissions__url': '/users/add/', 'permissions__code': 'add', 'permissions__group_id': 1}
                    {'permissions__title': '删除用户', 'permissions__url': '/users/del/(\\d+)/', 'permissions__code': 'del', 'permissions__group_id': 1}
                    {'permissions__title': '修改用户', 'permissions__url': '/users/edit/(\\d+)/', 'permissions__code': 'edit', 'permissions__group_id': 1}
                    {'permissions__title': '主机列表', 'permissions__url': '/hosts/', 'permissions__code': 'list', 'permissions__group_id': 2}
                    {'permissions__title': '添加主机', 'permissions__url': '/hosts/add/', 'permissions__code': 'add', 'permissions__group_id': 2}
                    {'permissions__title': '删除主机', 'permissions__url': '/hosts/del/(\\d+)/', 'permissions__code': 'del', 'permissions__group_id': 2}
                    {'permissions__title': '修改主机', 'permissions__url': '/hosts/edit/(\\d+)/', 'permissions__code': 'edit', 'permissions__group_id': 2}
                ]

                {
                    1(权限组ID): {
                        urls: [/u sers/,/users/add/ ,/users/del/(\d+)/],
                        codes: [list,add,del]
                    },
                    2: {
                        urls: [/hosts/,/hosts/add/ ,/hosts/del/(\d+)/],
                        codes: [list,add,del]
                    }
                }

                """
    # permission_list = UserInfo.roles.all(permissions__id__isnull=False).values(
    #     'permissions__title',
    #     'permissions__url',
    #     'permissions__code',
    #     'permissions__group_id',
    # ).distinct()
    # permission_list = UserInfo.roles.all()
    permission_list = UserInfo.objects.get(username='root').roles.all().values('permisions__id','permisions__url','permisions__code','permisions__code','permisions__group_id').distinct()

    # print(t,"$$$$$$ttttttt$$$$$",type(t))
    # permission_list = t.roles.all().values('permisions__id','permisions__url','permisions__code','permisions__code','permisions__group_id')


    # print("permission",type(permission_list),permission_list)
    permission_dict = {}
    for permission in permission_list:
        permisions__group_id = permission["permisions__group_id"]
        permission_dict[permisions__group_id]={}
        print(permission_dict)
        if permisions__group_id in permission_dict:
            print("in ex")

        else:
           print("####")


    print(permission_dict)

    #
    #         """           pass
    #
    #
    #
    #             {
    #                 1: {
    #                     urls: ['/users/', ],
    #                     codes: ['list',]
    #                 }
    #             }
    #         '''
    #
    return render(request, "user.html")
