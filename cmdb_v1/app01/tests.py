from django.test import TestCase
from django.shortcuts import render,HttpResponse,redirect
from  app01 import models
# Create your tests here.
# def host(request):
#     ##创建主机测试数据
#     for i in range(302):
#         dic ={"idc":"廊坊","sn":"12asdfadf","remoteip":"1.1.1.1",'hostname':'c%s.com' %(i,),"ip":'1.1.1.1'}
#         models.Host.objects.create(**dic)
#
#     # return render(request,'host.html')
#     return HttpResponse("创建成功")
