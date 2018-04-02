from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import redirect
from  rbac.models import UserInfo,Role
from django.conf import settings
from utils.md5 import  md5

# Create your views here.
from rbac.forms import UserModelForm,RoleModelForm

from utils.pager import Pagination
def user(request):
    all_count = UserInfo.objects.all().order_by('-id').count()
    per_page_count = request.GET.get('items')
    if not per_page_count:
        per_page_count = 20
        print("check per_page_count ", per_page_count)
    else:
        per_page_count = int(per_page_count)
        print(per_page_count,type(per_page_count))

    page_obj = Pagination(all_count,per_page_count,request.GET.get('page'),request_url=request.path_info)
    user_list = UserInfo.objects.all().order_by('-id')[page_obj.current_page_start_item:page_obj.current_page_end_item]

    return render(request, 'user.html', {'user_list': user_list, 'page_html': page_obj.page_html})


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

