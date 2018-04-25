from django.conf.urls import url
from django.shortcuts import HttpResponse,render,redirect
from django.urls import reverse
from django.forms import ModelForm

class StarkConfig(object):
    def __init__(self,model_class):
        self.model_class = model_class

    @property
    def urls(self):
        # self = StarkConfig(models.UserInfo) # obj.mcls = models.UserInfo
        # StarkConfig(models.Role),# # obj.model_class = models.Role
        patterns=[
            url(r'^$' ,self.changelist_view ),
            url(r'^add/$',self.add_view),
            url(r'^(\d+)/change/$',self.change_view),
            url(r'^(\d+)/delete/$',self.delete_view),
        ]
        patterns.extend(self.extra_url())

        return patterns

    def extra_url(self):
        """
        ##钩子函数
        :return:
        """

        return []

    def changelist_view(self,request):
        result_list=self.model_class.objects.all()
        # list_display=["name","email"]
        # for row in result_list:

        return render(request,"chagelist.html",{"result_list":result_list})
        # return HttpResponse('列表页面')
    def add_view(self,request):
        return HttpResponse('增加页面')
    def change_view(self,request,nid):
        return HttpResponse('编辑页面')
    def delete_view(self,request,nid):
        return HttpResponse('删除页面')


class StarkSite(object):
    def __init__(self):
        self._registry={}
    def registry(self,model_class,config_cls=None):
        if not  config_cls:
            config_cls = StarkConfig       ###默认是StarkConfi
        self._registry[model_class] = config_cls(model_class)
        # print(self._registry,"打印字典k") ###打印注册到字典 _registry的类
        # print(self._registry.items(),"打印字典v")

    def get_urls(self):
        pts = [
            url(r'^login/', self.login),
        ]

        for model_class,config_obj in self._registry.items():
            """
            _registry = {
                models.UserInfo: StarkConfig(models.UserInfo)，# 对象对象对象
                models.Role: StarkConfig(models.Role),# 对象对象对象
            }
            """

            app_label = model_class._meta.app_label
            model_name = model_class._meta.model_name
            print(app_label, model_name, "###############")
            temp = url(r'^%s/%s/' % (app_label, model_name),(config_obj.urls,None,None) )
            pts.append(temp)
        return pts

    @property
    def urls(self):
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
        return self.get_urls(), None,"stark"

    def login(self, request):
        return HttpResponse('登录页面')


site = StarkSite()

