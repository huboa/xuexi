
from django.conf.urls import url,include
from django.contrib import admin

from blog import views as blog_views



urlpatterns = [


    url(r'^article/(\d+)/$',blog_views.article_year ), # article_year(request,2009)
    url(r'^article/2003/$',blog_views.test ), # article_year(request,2009)

    # 无名分组
    url(r'article/(\d+)/(\d+)$',blog_views.article_yearMonth ), # article_yearMonth(request,2009,12)

    # named group
    url(r'article/(?P<year_id>\d+)/(?P<month_id>\d+)$',blog_views.article_yearMonth ), # article_yearMonth(request,year_id=2009,month_id=12)






]
