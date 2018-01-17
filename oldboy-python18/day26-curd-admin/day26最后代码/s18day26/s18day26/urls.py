"""s18day26 URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from crm import views

from monitor import views as mviews
from openstack import views as oviews
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^index/xxx/xxx/xx/xx/xx/', views.index,name='inx'),
    url(r'^ttt', views.ttt),
    # url(r'^login/', views.login),
    # url(r'^monitor/', include('monitor.urls',namespace='m')),
    # url(r'^openstack/', include('openstack.urls',namespace='o')),
    # /monitor/hosts/
    url(r'^login/', views.login),
    # url(r'^monitor/', ([
    #                         url(r'^hosts/',mviews.hosts,name='hhhhh'),
    #                         url(r'^c1/',mviews.hosts),
    #                         url(r'^x1/', ([
    #                                         url(r'^xxx1/',mviews.hosts),
    #                                         url(r'^xxx2/',mviews.hosts,name='xx2'),
    #                                         url(r'^xxx3/',mviews.hosts),
    #                                         url(r'^xxx4/',mviews.hosts),
    #                                       ],None,None)),
    #                         url(r'^c2/',mviews.hosts),
    #                         url(r'^c3/',mviews.hosts),
    #                    ],None,'mm')),
    # url(r'^openstack/', ([
    #                         url(r'^hosts/',oviews.hosts,name='hhhhh'),
    #                         url(r'^c1/',oviews.hosts),
    #                         url(r'^c2/',oviews.hosts),
    #                         url(r'^c3/',oviews.hosts),
    #                    ],None,'oo')),
]

for i in range(10):
    temp = []
    for j in range(5):
        temp.append(url(r'^inner_%s/' % j, views.login))
    v = url(r'^login_%s/' %i, (temp,None,None))
    urlpatterns.append(v)

