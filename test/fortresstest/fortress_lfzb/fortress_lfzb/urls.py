#from django.conf.urls import patterns, include, url
from django.conf.urls import  include, url
from django.contrib import admin
from django import views
admin.autodiscover()

urlpatterns = ('',
    # Examples:
    # url(r'^$', 'fortress_cd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
       (r'^grant/',views.grant),
       (r'^query/',views.query),
       (r'^login/',views.login),
       (r'^flow/',views.flow),
       (r'^wait/',views.wait),
       (r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root':'/home/mtime/fortress_lfzb/grant/static/images'}), 
)
