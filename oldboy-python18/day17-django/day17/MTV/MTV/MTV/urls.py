"""MTV URL Configuration

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

from blog import views as blog_views

from app01 import views as app01_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # url(r'^blog/article/(\d+)/$',blog_views.article_year ), # article_year(request,2009)
    # url(r'^blog/article/2003/$',blog_views.test ), # article_year(request,2009)

    # 无名分组
    #url(r'^blog/article/(\d+)/(\d+)$',blog_views.article_yearMonth ), # article_yearMonth(request,2009,12)

    # named group
    # url(r'^blog/article/(?P<year_id>\d+)/(?P<month_id>\d+)$',blog_views.article_yearMonth ), # article_yearMonth(request,year_id=2009,month_id=12)
    #
    #
    #  url(r"^app01/index",app01_views.index)

    # 路由分发app
    url(r'^blog/', include('blog.urls')),
    url(r'^login/', app01_views.login,name="LOGIN"),
    url(r'^index/', app01_views.index,name="index")


]


