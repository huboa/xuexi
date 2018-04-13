from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import redirect
from  rbac.models import UserInfo,Role
from django.conf import settings
from utils.md5 import  md5
import re

# Create your views here.
from rbac.forms import UserModelForm,RoleModelForm

from utils.pager import Pagination
def user(request):

    # 获取session中菜单信息，自动生成二级菜单【默认选中，默认展开】
    # menu_list = request.session.get(settings.PERMISSION_MENU_SESSION_KEY)
    # print(menu_list)
    # per_dict = {}
    #
    # current_url = request.path_info
    # for item in menu_list:
    #
    #     if item['id'] == item['pid']:
    #         per_dict[item['id']] = item
    #
    # for item in menu_list:
    #     reg = settings.REX_FORMAT % (item['url'])
    #     if not re.match(reg, current_url):
    #         continue
    #     # 匹配成功
    #     if item['pid']:
    #         per_dict[item['pid']]['active'] = True
    #     else:
    #         item['active'] = True
    # for item in per_dict.values():
    #     print(item)



    all_count = UserInfo.objects.all().order_by('-id').count() ####查到的总数
    per_page_count = request.GET.get('items')  ###每页显示条数
    get_page = request.GET.get('page')
    get_url = request.path_info
    if not per_page_count:
        per_page_count = 20  ##默认显示条数
    else:
        per_page_count = int(per_page_count)
    page_obj = Pagination(all_count,per_page_count,get_page,request_url=get_url)
    user_list = UserInfo.objects.all().order_by('-id')[page_obj.current_page_start_item:page_obj.current_page_end_item]


    return render(request, 'user.html', {'user_list': user_list, 'page_html': page_obj.page_html})
    return render(request, 'user.html')

def add_user(request):
    if request.method == "GET":
        form = UserModelForm()
        # return render(request,"add_host.html",{'form':form})
        return render(request,"add_user.html", {'form': form})
    else:
        form = UserModelForm(request.POST)

        if form.is_valid():
            form.cleaned_data['password'] = md5(form.cleaned_data['password'])
            # print(form.cleaned_data)

            form.save()
            username=form.cleaned_data['username']
            pwd = md5(form.cleaned_data['password'])
            UserInfo.objects.filter(username=username).update(password=pwd)
            return redirect("/user/")
        return render(request, "add_user.html", {'form': form})

def edit_user(request,nid):
    obj = UserInfo.objects.filter(id=nid).first()
    if not obj:
        return HttpResponse('数据不存在')
    if request.method == "GET":
        form = UserModelForm(instance=obj)
        return  render(request,'edit_host.html',{"form":form})
    else:
        form = UserModelForm(data=request.POST, instance=obj)
        if form.is_valid():
            pwd = md5(form.cleaned_data['password'])

            form.save()
            print(form.cleaned_data)
            UserInfo.objects.filter(id=nid).update(password=pwd)
            return redirect('/user/')
        return render(request, 'edit_user.html', {'form': form})

def del_user(request,nid):
    obj = UserInfo.objects.filter(id=nid).first()
    if not obj:
        return HttpResponse('数据不存在')
    else:
        UserInfo.objects.filter(id=nid).delete()
        return redirect('/user/')

def role(request):
    all_count = Role.objects.all().order_by('-id').count()
    per_page_count = request.GET.get('items')
    if not per_page_count:
        per_page_count = 20
        # print("check per_page_count ", per_page_count)
    else:
        per_page_count = int(per_page_count)
        # print(per_page_count,type(per_page_count))

    page_obj = Pagination(all_count,per_page_count,request.GET.get('page'),request_url=request.path_info)
    role_list = Role.objects.all().order_by('-id')[page_obj.current_page_start_item:page_obj.current_page_end_item]

    return render(request, 'role.html', {'role_list': role_list, 'page_html': page_obj.page_html})

def add_role(request):
    if request.method == "GET":
        add_role_form = RoleModelForm()
        return render(request,"add_role.html", {'add_role_form': add_role_form})
    else:
        add_role_form = RoleModelForm(request.POST)
        if add_role_form.is_valid():
            add_role_form.save()
            return redirect("/role/")
        return render(request, "add_role.html", {'add_role_form': add_role_form})


def edit_role(request,nid):
    obj = Role.objects.filter(id=nid).first()
    if not obj:
        return HttpResponse('数据不存在')
    if request.method == "GET":
        form = RoleModelForm(instance=obj)
        return  render(request,'edit_role.html',{"form":form})
    else:
        form = RoleModelForm(data=request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/role/')
        return render(request, 'edit_role.html', {'form': form})

def del_role(request,nid):
    obj = Role.objects.filter(id=nid).first()
    if not obj:
        return HttpResponse('数据不存在')
    else:
        Role.objects.filter(id=nid).delete()
        return redirect('/user/')
