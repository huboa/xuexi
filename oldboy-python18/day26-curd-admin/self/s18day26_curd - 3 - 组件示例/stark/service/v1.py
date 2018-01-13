from django.conf.urls import url
from django.shortcuts import HttpResponse,render
class StarkConfig(object):
    """
    用于封装  单独数据库操作类
    """
    def __init__(self,mcls):
        self.mcls = mcls

    @property
    def urls(self):
        # self = StarkConfig(models.UserInfo) # obj.mcls = models.UserInfo

        # StarkConfig(models.Role),# # obj.mcls = models.Role
        patterns =[
            url(r'^$',self.changelist_view),
            url(r'^add/$',self.add_view),
            url(r'^(\d+)/change/$',self.change_view),
            url(r'^(\d+)/delete/$',self.delete_view),
        ]

        patterns.extend(self.extra_url())

        return patterns

    def extra_url(self):
        """
        钩子函数
        :return:
        """
        return []

    def changelist_view(self,request):
        """
        /stark/app01/userinfo/
        /stark/app01/userinfo/add/
        /stark/app01/userinfo/1/change/
        /stark/app01/userinfo/1/delete/

        self.mcls = models.UserInfo


        /stark/app01/role/
        /stark/app01/role/add/
        /stark/app01/role/1/change/
        /stark/app01/role/1/delete/

        self.mcls = models.Role

        :param request:
        :return:
        """
        result_list = self.mcls.objects.all()
        return render(request,'changelist.html',{'result_list':result_list})
    def add_view(self,request):
        return HttpResponse('添加页面')
    def change_view(self,request,nid):
        return HttpResponse('修改页面')
    def delete_view(self,request,nid):
        return HttpResponse('删除页面')


class StarkSite(object):
    """
    用于封装所有的   数据库操作类
    """
    def __init__(self):
        self._registry = {}

    def register(self,model_class,config_cls=None):
        # models.UserInfo,UserInfoConfig
        if not config_cls:
            config_cls = StarkConfig
        self._registry[model_class] = config_cls(model_class)

    @property
    def urls(self):
        from django.conf.urls import url
        pts = [
            url(r'^login/', self.login),
        ]
        """
        _registry = {
            models.UserInfo: StarkConfig(models.UserInfo),
            models.Role: StarkConfig(models.Role),
        }
        
        # /admin//app01/userinfo/           查看列表页面
        # /admin/app01/userinfo/add/        添加页面
        # /admin/app01/userinfo/1/change/   修改页面
        # /admin/app01/userinfo/1/delete/   删除页面
        
        
        /stark/   ->  ([
                            /login/
                            /app01/userinfo/  --> ([
                                                        /                    查看列表
                                                        add/                 添加
                                                        (\d+)/change/        修改
                                                        (\d+)/delete/        删除
                                                    ])
                            /app01/role/
                                                --> ([
                                                        /                   查看列表
                                                        add/                添加
                                                        (\d+)/change/        修改
                                                        (\d+)/delete/        删除
                                                    ])
                        ])

        """
        for model_class,config_obj in self._registry.items():
            """
            _registry = {
                models.UserInfo: StarkConfig(models.UserInfo)，# 对象对象对象
                models.Role: StarkConfig(models.Role),# 对象对象对象
            }
            """
            app_label = model_class._meta.app_label
            model_name = model_class._meta.model_name
            # models.UserInfo: StarkConfig(models.UserInfo) # obj.mcls = models.UserInfo
            # config_obj.urls，对象的urls方法

            # models.Role: StarkConfig(models.Role),# # obj.mcls = models.Role
            # config_obj.urls，对象的urls方法
            temp = url(r'^%s/%s/' %(app_label,model_name), (config_obj.urls,None,None))
            pts.append(temp)

        return pts,None,None

    def login(self,request):
        return HttpResponse('登录页面')

site = StarkSite()