from django.shortcuts import render,HttpResponse

# Create your views here.

def hosts(request):
    return HttpResponse('监控系统，主机列表')