
from django import template
from django.utils.safestring import mark_safe

register = template.Library()  # register的名字是固定的,不可改变





@register.filter  # 定义过滤器
def multi(x,y):

    return x*y


@register.simple_tag   # 定义标签
def multi_tag(x,y,z):
    return x*y*z

