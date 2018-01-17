from django.conf.urls import url
from django.shortcuts import HttpResponse,render,redirect
from django.urls import reverse
from django.forms import ModelForm
class StarkConfig(object):
    """
    用于封装  单独数据库操作类
    """
    list_display = []
    model_form_cls = None

    def get_model_form_cls(self):
        if self.model_form_cls:
            return self.model_form_cls

        class TempModelForm(ModelForm):
            class Meta:
                model = self.mcls
                fields = "__all__"

        return TempModelForm
    def __init__(self,mcls):
        self.mcls = mcls

    @property
    def urls(self):
        # self = StarkConfig(models.UserInfo) # obj.mcls = models.UserInfo
        # StarkConfig(models.Role),# # obj.mcls = models.Role

        app_model_name = (self.mcls._meta.app_label, self.mcls._meta.model_name,)

        patterns =[
            url(r'^$',self.changelist_view,name='%s_%s_changelist' %app_model_name),
            url(r'^add/$',self.add_view,name='%s_%s_add'  %app_model_name),
            url(r'^(\d+)/change/$',self.change_view,name="%s_%s_change"  %app_model_name),
            url(r'^(\d+)/delete/$',self.delete_view,name="%s_%s_delete"  %app_model_name),
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
        result_list = self.mcls.objects.all()

        # 处理表头
        header_list = []
        for n in self.list_display:
            val = self.mcls._meta.get_field(n).verbose_name
            header_list.append(val)

        # 处理表内容
        body_list = []
        for row in result_list:
            temp = []
            for n in self.list_display:
                temp.append(getattr(row,n))
            body_list.append(temp)

        # 处理添加按钮的URL
        # self.mcls
        app_model_name = (self.mcls._meta.app_label, self.mcls._meta.model_name,)
        name = "stark:%s_%s_add" %app_model_name
        add_url = reverse(name)
        return render(request,'changelist.html',{'body_list':body_list,'header_list':header_list,'add_url':add_url})
    def add_view(self,request):
        # self.mcls # models.UserInfo
        # self.mcls # models.Role
        # self.mcls # models.Group

        model_form_class = self.get_model_form_cls()

        if request.method == "GET":
            form = model_form_class()
            return render(request,'add_view.html',{'form':form})
        else:
            form = model_form_class(request.POST)
            if form.is_valid():
                form.save()
                # 跳转到列表页面
                app_model_name = (self.mcls._meta.app_label, self.mcls._meta.model_name,)
                name = "stark:%s_%s_changelist" % app_model_name
                list_url = reverse(name)
                return redirect(list_url)

            return render(request, 'add_view.html', {'form': form})
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

        return pts,None,"stark"

    def login(self,request):
        return HttpResponse('登录页面')

site = StarkSite()