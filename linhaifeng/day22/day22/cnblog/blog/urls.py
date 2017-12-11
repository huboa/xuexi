
from django.conf.urls import url,include
from django.contrib import admin
from blog import views
from django.views.static import serve
from cnblog import settings

urlpatterns = [

    url(r'^diggit/', views.diggit),
    # 设计文章详细页的url
    url(r'^(?P<username>\w+)/articles/(?P<article_id>\d+)', views.articleDetail),

    # 访问个人站点下的归档信息
    url(r'^(?P<username>\w+)/(?P<condition>category|tag|date)/(?P<para>.*)', views.homeSite),
    # homeSite(request,username="yaun",condition="tag",para="2017-12")

    # 访问个人站点首页
    url(r'^(?P<username>.+)/', views.homeSite),  # homeSite(request,username="yaun")


]
