from django.conf.urls import url
from django.shortcuts import HttpResponse,render,redirect
from django.urls import reverse
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from types import FunctionType
from utils.pager import Pagination

class ChangeList(object):
    """
    用于对列表页面的功能做拆分
    """
    def __init__(self,config,result_list,request):
        """
        :param config: 处理每个表增伤改查功能的对象
        :param result_list: 从数据库查询到的数据
        """
        self.config = config

        self.request = request

        all_count = result_list.count()
        page_obj = Pagination(request.GET.get('page'), all_count, request.path_info)
        self.result_list = result_list[page_obj.start:page_obj.end]
        self.page_obj = page_obj

    def header_list(self):
        """
        处理页面表头的内容
        :return:
        """
        result = []
        # ['id', 'name', 'email',display_edit,display_del]
        # ['ID', '用户名', '邮箱','临时表头',临时表头]

        for n in self.config.get_list_display():
            if isinstance(n, FunctionType):
                # 执行list_display中的函数
                val = n(self.config, is_header=True)
            else:
                val = self.config.mcls._meta.get_field(n).verbose_name
            result.append(val)

        return result

    def body_list(self):
        """
        处理页面表内容
        :return:
        """
        result = []
        """
        [
            obj,
            obj,
            obj,
        ]
        # ['id', 'name', 'email',display_edit,display_del]
        [
            [1, '天了','123@liv.com'],
            [2, '天1了','123@liv.com'],
            [3, '天了123','123@liv.com'],
        ]
        """
        for row in self.result_list:
            temp = []
            for n in self.config.get_list_display():
                if isinstance(n, FunctionType):
                    val = n(self.config, row=row)
                else:
                    val = getattr(row, n)
                temp.append(val)
            result.append(temp)
        return result

    def add_url(self):
        """
        生成添加按钮
        :return:
        """
        # 处理添加按钮的URL
        # self.mcls
        app_model_name = (self.config.mcls._meta.app_label, self.config.mcls._meta.model_name,)
        name = "stark:%s_%s_add" % app_model_name
        add_url = reverse(name)
        return add_url

class StarkConfig(object):
    """
    用于封装  单独数据库操作类
    """
    def display_checkbox(self,is_header=False,row=None):
        if is_header:
            return '选择'
        return mark_safe("<input type='checkbox' name='pk' value='%s' />" %(row.id,))

    def display_edit(self, is_header=False, row=None):
        if is_header:
            return "编辑"
        app_model_name = (self.mcls._meta.app_label, self.mcls._meta.model_name,)
        name = "stark:%s_%s_change" % app_model_name
        url_path = reverse(name, args=(row.id,))
        return mark_safe('<a href="%s">编辑</a>' % (url_path,))

    def display_del(self, is_header=False, row=None):
        if is_header:
            return "删除"

        app_model_name = (self.mcls._meta.app_label, self.mcls._meta.model_name,)
        name = "stark:%s_%s_delete" % app_model_name
        url_path = reverse(name, args=(row.id,))
        return mark_safe('<a href="%s">删除</a>' % (url_path,))


    list_display = []
    def get_list_display(self):
        result = []
        if self.list_display:
            result.extend(self.list_display)
            result.insert(0,StarkConfig.display_checkbox)
            result.append(StarkConfig.display_edit)
            result.append(StarkConfig.display_del)
        return result


    model_form_cls = None

    def get_model_form_cls(self):
        """
        如果类中定义了 model_form_cls，则使用；否则创建TempModelForm
        :return:
        """
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

    # ############# 反向生成URL开始 ##################
    def get_edit_url(self,pk):
        # /stark/app01/userinfo/1/change/
        # /stark/app02/role/1/change/
        app_model_name = (self.mcls._meta.app_label, self.mcls._meta.model_name,)
        name = "stark:%s_%s_change"  %app_model_name
        url_path = reverse(name,args=(pk,))
        return url_path

    def get_delete_url(self,pk):
        # /stark/app01/userinfo/1/delete/
        # /stark/app02/role/1/delete/
        app_model_name = (self.mcls._meta.app_label, self.mcls._meta.model_name,)
        name = "stark:%s_%s_delete"  %app_model_name
        url_path = reverse(name,args=(pk,))
        return url_path

    def get_changlist_url(self):
        # /stark/app01/userinfo/1/delete/
        # /stark/app02/role/1/delete/
        app_model_name = (self.mcls._meta.app_label, self.mcls._meta.model_name,)
        name = "stark:%s_%s_changelist"  %app_model_name
        url_path = reverse(name)
        return url_path

    # ############# 反向生成URL结束 ##################

    def extra_url(self):
        """
        钩子函数
        :return:
        """
        return []

    def changelist_view(self,request):
        """
        列表页面
        :param request:
        :return:
        """
        result_list = self.mcls.objects.all()
        cl = ChangeList(self,result_list,request)

        return render(request,'changelist.html',{'cl':cl})
    def add_view(self,request):
        """
        添加页面
        :param request:
        :return:
        """
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
        """
        编辑页面
        :param request:
        :param nid:
        :return:
        """
        obj = self.mcls.objects.filter(pk=nid).first()
        if not obj:
            return HttpResponse('别闹')

        model_form_cls = self.get_model_form_cls()
        if request.method == "GET":
            form = model_form_cls(instance=obj)
            return render(request,'change_view.html',{'form':form})
        else:
            form = model_form_cls(instance=obj,data=request.POST)
            if form.is_valid():
                form.save()
                return redirect(self.get_changlist_url())
            return render(request, 'change_view.html', {'form': form})


    def delete_view(self,request,nid):
        self.mcls.objects.filter(id=nid).delete()
        path = self.get_changlist_url()
        return redirect(path)

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