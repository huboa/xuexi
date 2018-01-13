from  django.shortcuts import HttpResponse
from django.conf.urls import url

class StarkConfig(object):
    def __init__(self,mcls):
        self.mcls = mcls
    @property
    def urls(self):
        patterns=[
            url(r'^$',self.chagelist_view),
            url(r'^add/$', self.add_view),
            url(r'^(\d+)/change/$', self.change_view),
            url(r'^(\d+)/delete/$', self.delete_view),

        ]
        return patterns

    def changelist_view(self,request):
        return HttpResponse('列表页面')
    def add_view(self,request):
        return HttpResponse('添加页面')
    def change_view(self,request):
        return HttpResponse('修改页面')
    def delete_view(self,request):
        return HttpResponse('删除页面')



class StarkSite(object):
    def __init__(self):
        self._registry ={}


    def register(self,model_class):
        self.registry[model_class] = StarkConfig(model_class)

    @property
    def urls(self):
        from django.conf.urls import url
        pts = [
            url(r'^login/',self.login),
        ]

        for model_class,config_obj in self._registry.items():
            app_label = model_class._meta.app_label
            model_name = model_class._meta.model_name
            temp = url(r'^%s/%s/' %(app_label,model_name),(config_obj.url,None,None))
            pts.append(temp)

        return pts,None,None

    def login(self,request):
        return HttpResponse('登录页面')


site = StarkSite()

