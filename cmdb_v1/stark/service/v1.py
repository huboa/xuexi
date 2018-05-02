from django.conf.urls import url
from django.shortcuts import HttpResponse,render,redirect
from django.urls import reverse
from django.forms import ModelForm
from types import FunctionType
from django.utils.safestring import mark_safe


class ChangeList(object):
    """
    用于对列表页面的功能做拆分
    """
    def __init__(self,config,result_list):
        """
        :param config: 处理每个表增伤改查功能的对象
        :param result_list: 从数据库查询到的数据
        """
        self.config = config
        self.result_list = result_list

    # 处理表头
    def header_list(self):
        """
               处理页面表头的内容
               :return:
               """
        result = []
        for n in self.config.get_list_display():#####1111122222
            if isinstance(n,FunctionType):
                print(n,type(n),"header_list$$$$$")
                val = n(self,is_header=True)    ###执行函数
            else:
                val = self.config.model_class._meta.get_field(n).verbose_name   ###去model 取数据
            result.append(val)
        print(result,"header_list#####")
        return result

    # 处理表内容
    def body_list(self):
        """
        处理页面表内容
        :return:
        """
        result = []
        for row in self.result_list:
            print("row=",row,type(row))
            temp = []
            for n in self.config.get_list_display():
                if isinstance(n, FunctionType):
                    val = n(self.config,row=row)
                else:
                    val = getattr(row, n)
                temp.append(val)
            result.append(temp)
        return result

    # 处理添加按钮的URL
    def add_url(self):
        """
               生成添加按钮
               :return:
               """
        app_model_name = (self.config.model_class._meta.app_label, self.config.model_class._meta.model_name,)
        name = "stark:%s_%s_add" % app_model_name
        add_url = reverse(name)
        return add_url


class StarkConfig(object):
    """
    用于封装  单独数据库操作类
    """
    #按钮级别的 url
    def display_checkbox(self, is_header=False, row=None):
        if is_header:
            return '选择'
        return mark_safe("<input type='checkbox' name='pk' value='%s' />" % (row.id,))
    def display_edit(self,is_header=False,row=None):
        if is_header:
            return "编辑"

        app_model_name = (self.model_class._meta.app_label, self.model_class._meta.model_name,)
        name = "stark:%s_%s_change" % app_model_name
        url_path = reverse(name, args=(row.id,))
        return mark_safe('<a href=%s>编辑</a>'%(url_path))
    def display_delete(self,is_header=False,row=None):
        if is_header:
            return '删除'
        app_model_name = (self.model_class._meta.app_label, self.model_class._meta.model_name,)
        name = "stark:%s_%s_delete" % app_model_name
        url_path = reverse(name, args=(row.id,))
        return mark_safe('<a href=%s>删除</a>' % (url_path))

    list_display = []

    ###整合stark 字符串 和 函数 display 方法
    def get_list_display(self):
        result = []
        if self.list_display:
            result.extend(self.list_display)
            result.insert(0,StarkConfig.display_checkbox)
            result.append(StarkConfig.display_edit)
            result.append(StarkConfig.display_delete)

        return result

    model_form_cls = None   ###表单类

    def __init__(self,model_class):
        self.model_class = model_class

    def get_model_form_cls(self):
        if self.model_form_cls:
            return self.model_form_cls

        class TempModelForm(ModelForm):
            class Meta:
                model = self.model_class
                fields = "__all__"

        return TempModelForm


    @property
    def urls(self):
        # self = StarkConfig(models.UserInfo) # obj.mcls = models.UserInfo
        # StarkConfig(models.Role),# # obj.model_class = models.Role
        app_model_name = (self.model_class._meta.app_label, self.model_class._meta.model_name,)   ###反向生成 url 用

        patterns=[
            url(r'^$' ,self.changelist_view ,name='%s_%s_changelist' %app_model_name),
            url(r'^add/$',self.add_view,name='%s_%s_add'  %app_model_name),
            url(r'^(\d+)/change/$',self.change_view,name="%s_%s_change"  %app_model_name),
            url(r'^(\d+)/delete/$',self.delete_view,name="%s_%s_delete"  %app_model_name),
        ]
        patterns.extend(self.extra_url())

        return patterns

    def extra_url(self):
        """
        ##钩子函数
        :return:
        """
        return []

    # ############# 反向生成URL开始 ##################
    def get_edit_url(self,pk):
        """
        /stark/app01/userinfo/1/
        :param pk:
        :return:
        """
        app_model_name = (self.model_class._meta.app_label, self.model_class._meta.model_name,)
        name = "stark:%s_%s_change"  %app_model_name
        url_path =reverse(name,args=(pk,))
        return url_path

    def get_delete_url(self, pk):
        """
        /stark/app01/userinfo/1/
        :param pk:
        :return:
        """
        app_model_name = (self.model_class._meta.app_label, self.model_class._meta.model_name,)
        name = "stark:%s_%s_delete" % app_model_name
        url_path = reverse(name, args=(pk,))
        return url_path

    def get_changlist_url(self):
        # /stark/app01/userinfo/1/delete/
        # /stark/app02/role/1/delete/
        app_model_name = (self.model_class._meta.app_label, self.model_class._meta.model_name,)
        name = "stark:%s_%s_changelist"  %app_model_name
        url_path = reverse(name)
        return url_path

    # ############# 反向生成URL结束 ##################
    ##########四个视图开始##########
    def changelist_view(self,request):

        """

        备份ChangeList，如果 弄不出来恢复注释内容删除 注释后面代码
        result_list = self.model_class.objects.all()
        # list_display=["name","email"]
        # for row in result_list:

        # # 处理表头
        # header_list = []
        # for n in self.get_list_display():#####1111122222
        #     if isinstance(n,FunctionType):
        #         print(n,type(n),"header_list$$$$$")
        #         val = n(self,is_header=True)    ###执行函数
        #     else:
        #         val = self.model_class._meta.get_field(n).verbose_name   ###去model 取数据
        #     header_list.append(val)
        # print(header_list,"header_list#####")
        # # 处理表内容
        # body_list = []
        # for row in result_list:
        #     temp = []
        #     for n in self.get_list_display():
        #         if isinstance(n, FunctionType):
        #             val = n(self,row=row)
        #         else:
        #             val = getattr(row, n)
        #         temp.append(val)
        #     body_list.append(temp)
        # print(body_list,"bodylist###")
        #
        # # 处理添加按钮的URL
        # # self.model_class
        # app_model_name = (self.model_class._meta.app_label, self.model_class._meta.model_name,)
        # name = "stark:%s_%s_add" % app_model_name
        # add_url = reverse(name)
        #
        # # return render(request, 'changelist.html', {'body_list': body_list, 'header_list': header_list,})
        # return render(request, 'changelist.html', {'body_list': body_list, 'header_list': header_list, 'add_url': add_url})
    """
        result_list = self.model_class.objects.all()
        cl = ChangeList(self, result_list)
        return render(request, 'changelist.html', {'cl': cl})

    def add_view(self,request):
        # self.mcls # models.UserInfo
        # self.mcls # models.Role
        # self.mcls # models.Group

        model_form_class = self.get_model_form_cls()

        if request.method == "GET":
            form = model_form_class()
            return render(request, 'add_view.html', {'form': form})
        else:
            form = model_form_class(request.POST)
            if form.is_valid():
                form.save()
                # 跳转到列表页面
                app_model_name = (self.model_class._meta.app_label, self.model_class._meta.model_name,)
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
        obj = self.model_class.objects.filter(pk=nid).first()
        if not obj:
            return HttpResponse('别闹')

        model_form_cls = self.get_model_form_cls()
        if request.method == "GET":
            form = model_form_cls(instance=obj)
            return render(request, 'change_view.html', {'form': form})
        else:
            form = model_form_cls(instance=obj, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect(self.get_changlist_url())
            return render(request, 'change_view.html', {'form': form})

    def delete_view(self,request,nid):
        self.model_class.objects.filter(id=nid).delete()
        path = self.get_changlist_url()
        return redirect(path)
    ###########四个视图结束##########

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

