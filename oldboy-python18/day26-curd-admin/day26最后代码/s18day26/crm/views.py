from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse

def index(request):
    return HttpResponse('Index')

def login(request):
    return HttpResponse('Login')
def ttt(request):
    url = reverse('inx')
    return redirect(url)


    # 跳转到 openstack主机列表页面
    # return redirect('/openstack/hosts/')
    # url = reverse('o:hosts')
    # url = reverse('oo:hhhhh')
    # url = reverse('mm:uu:xx2')
    # return redirect(url)


def hosts(request):
    return HttpResponse('主机列表')