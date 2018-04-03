"""mtime_cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views
from rbac import views as rbac_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$',views.login),
    url(r'^index/$', views.index),
    url(r'^host/$', views.host),
    url(r'^host/add/$', views.add_host),
    url(r'^host/edit/(\d+)/$', views.edit_host),
    url(r'^host/del/(\d+)/$', views.del_host),
    url(r'^user/$', rbac_views.user),
    url(r'^user/add/$', rbac_views.add_user),
    url(r'^user/edit/(\d+)/$', rbac_views.edit_user),
    url(r'^user/del/(\d+)/$', rbac_views.del_user),
    url(r'^role/$', rbac_views.role),
    url(r'^role/add/$', rbac_views.add_role),
    url(r'^role/edit/(\d+)/$', rbac_views.edit_role),
    url(r'^role/del/(\d+)/$', rbac_views.del_role),
]
