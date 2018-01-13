def register(self,model_class):
    self.registry[model_class] = StarkConfig(model_class)

@property
def url(self):
    from django.conf.urls import url
    pts = [
        url(r'^login/',self.login),
    ]

    for model_class,config_obj in self._registry.items():
        app_label = model_class._meta.app_label
        model_name = model_class._meta.model_name
        temp = url(r'^%s/%s/' %(app_label,model_name),self.login)
        pts.append(temp)

    return pts,None,None

def login(self,request):
    return HttpResponse('登录页面')


site = StarkSite()

