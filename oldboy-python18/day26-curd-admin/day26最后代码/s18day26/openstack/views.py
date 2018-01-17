from django.shortcuts import render,HttpResponse

# Create your views here.

def hosts(request):
    return HttpResponse('OpenStack，主机列表')