from django.conf.urls import url
from django.shortcuts import HttpResponse,render,redirect
from django.urls import reverse
from django.forms import ModelForm
from types import FunctionType
from django.utils.safestring import mark_safe

from utils.pager import Pagination

<<<<<<< HEAD
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
=======
>>>>>>> 4dcc1d9b1c975aa27c0af1e30f556f03da6f59e7

class GetListView(object):
    """
    用于对列表页面的功能做拆分
    """
<<<<<<< HEAD
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
=======
    def __init__(self,config,result_list,request):
        """
        :param config: 处理每个表增伤改查功能的对象
        :param result_list: 从数据库查询到的数据
        """
        self.config = config
        self.result_list = result_list
>>>>>>> 4dcc1d9b1c975aa27c0af1e30f556f03da6f59e7

        page_obj=Pagination(request,self.result_list)  ##实例化页码对象
        self.page_list = page_obj.page_obj_list()    ##每页的 20对象
        self.page_html=mark_safe(page_obj.bootstrap_page_html())  ##实例化页码导航


<<<<<<< HEAD
    model_form_cls = None   ###表单类

    def __init__(self,model_class):
=======
        # page_obj = Pagination(request.GET.get('page'), all_count, request.path_info)
        # self.result_list = result_list[page_obj.start:page_obj.end]
        # self.page_html = page_obj

    def header_list(self):
        """
        处理页面表头的内容
        :return:
        """
        result = []
        # ['id', 'name', 'email',display_change,display_del]
        # ['ID', '用户名', '邮箱','临时表头',临时表头]

        for n in self.config.get_list_display():
            if isinstance(n, FunctionType):
                # 执行list_display中的函数
                val = n(self.config, is_header=True)
            else:
                val = self.config.model_class._meta.get_field(n).verbose_name
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
        # ['id', 'name', 'email',display_change,display_del]
        [
            [1, '天了','123@liv.com'],
            [2, '天1了','123@liv.com'],
            [3, '天了123','123@liv.com'],
        ]
        """
        for row in self.page_list:
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
        返回添加按钮的URL
        """
        return self.config.get_add_url()

class StarkConfig(object):
    """
    初始化类数据
    """
    def __init__(self, model_class):
>>>>>>> 4dcc1d9b1c975aa27c0af1e30f556f03da6f59e7
        self.model_class = model_class

    model_form_cls = None   ###表单类
    def get_model_form_cls(self):
        if self.model_form_cls:
            return self.model_form_cls

        class TempModelForm(ModelForm):
             class Meta:
                 model = self.model_class
                 fields = "__all__"
        return TempModelForm

######生成路由url 处理########################
    @property
    def urls(self):
        # self = StarkConfig(models.UserInfo) # obj.mcls = models.UserInfo
        # StarkConfig(models.Role),# # obj.model_class = models.Role
        app_model_name = (self.model_class._meta.app_label, self.model_class._meta.model_name,)  ###反向生成 url 用

        patterns = [
            url(r'^$', self.get_list_view, name='%s_%s_get_list' % app_model_name),
            url(r'^add/$', self.add_view, name='%s_%s_add' % app_model_name),
            url(r'^(\d+)/change/$', self.change_view, name="%s_%s_change" % app_model_name),
            url(r'^(\d+)/delete/$', self.delete_view, name="%s_%s_delete" % app_model_name),
        ]
        patterns.extend(self.extra_url())

        return patterns
    def extra_url(self):
        """
        ##钩子函数
        :return:
        """
        return []

<<<<<<< HEAD
    # ############# 反向生成URL开始 ##################
    def get_edit_url(self,pk):
=======
############ 获取反向生成的URL---开始 ##################
    def get_change_url(self, pk):
>>>>>>> 4dcc1d9b1c975aa27c0af1e30f556f03da6f59e7
        """
        /stark/app01/userinfo/1/
        :param pk:
        :return:
        """
        app_model_name = (self.model_class._meta.app_label, self.model_class._meta.model_name,)
<<<<<<< HEAD
        name = "stark:%s_%s_change"  %app_model_name
        url_path =reverse(name,args=(pk,))
=======
        name = "stark:%s_%s_change" % app_model_name
        url_path = reverse(name, args=(pk,))
>>>>>>> 4dcc1d9b1c975aa27c0af1e30f556f03da6f59e7
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
<<<<<<< HEAD

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
=======
    def get_list_url(self):
        # /stark/app01/userinfo/1/delete/
        # /stark/app02/role/1/delete/
        app_model_name = (self.model_class._meta.app_label, self.model_class._meta.model_name,)
        name = "stark:%s_%s_get_list" % app_model_name
        url_path = reverse(name)
        return url_path
    def get_add_url(self):
        app_model_name = (self.model_class._meta.app_label, self.model_class._meta.model_name,)
        name = "stark:%s_%s_add" % app_model_name
        url_path = reverse(name)
        return url_path

#####增删改查页面视图####
    def get_list_view(self,request):

        ##备份
        """
        result_list=self.model_class.objects.all()
>>>>>>> 4dcc1d9b1c975aa27c0af1e30f556f03da6f59e7
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

<<<<<<< HEAD
=======
        # return render(request, 'get_list_view.html', {'body_list': body_list, 'header_list': header_list,})
        return render(request, 'get_list_view.html', {'body_list': body_list, 'header_list': header_list, 'add_url': add_url})
        """

        result_list = self.model_class.objects.all()
        cl = GetListView(self,result_list,request)
        return render(request, "get_list_view.html", {"cl":cl})
>>>>>>> 4dcc1d9b1c975aa27c0af1e30f556f03da6f59e7
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
                return redirect(self.get_list_url())

            return render(request, 'add_view.html', {'form': form})


    def change_view(self,request,nid):
<<<<<<< HEAD
        """
               编辑页面
               :param request:
               :param nid:
               :return:
               """
=======

>>>>>>> 4dcc1d9b1c975aa27c0af1e30f556f03da6f59e7
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
<<<<<<< HEAD
                return redirect(self.get_changlist_url())
            return render(request, 'change_view.html', {'form': form})

    def delete_view(self,request,nid):
        self.model_class.objects.filter(id=nid).delete()
        path = self.get_changlist_url()
        return redirect(path)
    ###########四个视图结束##########
=======
                return redirect(self.get_list_url())
            return render(request, 'change_view.html', {'form': form})
    def delete_view(self,request,nid):
        self.model_class.objects.filter(id=nid).delete()
        return redirect(self.get_list_url())

#处理按钮的 url
    def display_checkbox(self, is_header=False, row=None):
        if is_header:
            return '选择'
        return mark_safe("<input type='checkbox' name='pk' value='%s' />" % (row.id,))
    def display_change(self,is_header=False,row=None):
        if is_header:
            return "编辑"
        url_path = self.get_change_url(pk=row.id)
        return mark_safe('<a href=%s>编辑</a>'%(url_path))
    def display_delete(self,is_header=False,row=None):
        if is_header:
            return '删除'
        url_path = self.get_delete_url(pk=row.id)
        return mark_safe('<a href=%s>删除</a>' % (url_path))

# 控制显示列表  整合stark 字符串 和 函数 display 方法
    list_display = []
    def get_list_display(self):
        result = []
        if self.list_display:
            result.extend(self.list_display)
            result.insert(0, StarkConfig.display_checkbox)
            result.append(StarkConfig.display_change)
            result.append(StarkConfig.display_delete)
        return result
>>>>>>> 4dcc1d9b1c975aa27c0af1e30f556f03da6f59e7

class StarkSite(object):
    """
    注册所有表的 url
    """
    def __init__(self):
        self._registry={}
    def registry(self,model_class,config_cls=None):
        if not  config_cls:
            config_cls = StarkConfig       ###默认是StarkConfi
        self._registry[model_class] = config_cls(model_class)
        # print(self._registry,"打印字典k") ###打印注册到字典 _registry的类
        # print(self._registry.items(),"打印字典v")

    def get_urls(self):
        """
        生成所有注册的路由信息url
        :return:
        """
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

###单例模式只生成一次
site = StarkSite()

