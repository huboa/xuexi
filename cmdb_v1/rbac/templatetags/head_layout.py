
from django.shortcuts import render,HttpResponse,redirect
from rbac.service.init_permissions import user_state
from django.template import Library
register = Library()

####根据用户登录状态生成 登录或退出url
@register.inclusion_tag('head_layout.html')
def head_layout():
    # request_host = (request.get_host())
    request_host = "127.0.0.1:8000"
    if not user_state:
        print("已经登陆",user_state())
        head_url = str(request_host)+"/logout/"
    else:
        print("没有登录")
        head_url = str(request_host)+"/login/"

    return {"log_url": head_url}