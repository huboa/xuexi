from django.shortcuts import render,HttpResponse
from app01 import models
def test(request):
    app_label = models.Role._meta.app_label
    model_name = models.Role._meta.model_name
    print(app_label,model_name)
    return HttpResponse('xxx')
