from django.conf.urls import url
from django.shortcuts import HttpResponse,render,redirect
from django.urls import reverse
from django.forms import ModelForm
from types import FunctionType
from django.utils.safestring import mark_safe
from utils.pager import Pagination
from django.db.models import Q
import copy
from rbac import models
from django.db.models.fields.related import ForeignKey
from django.http import QueryDict
from django.conf import settings

####组合搜索类
class FilterRow(object):
    def __init__(self,_field,name,request,get_list_url,is_choice=False):
        '''

        :param _field: queryset类型 取字段
        :param name: 字段名称
        :param request: 请求
        :param get_list_url: 获取当前url
        :param is_choice: 是不是从数据取
        '''
        self.request = request
        self._field = _field
        self.is_choince = is_choice
        self.name = name
        self.params = copy.deepcopy( self.request.GET)
        self.params._mutable = True
        self.get_list_url=get_list_url
    def __iter__(self):
        if self.name in self.params:
            ori_nid = self.params.get(self.name)
            self.params.pop(self.name)
            yield mark_safe("<a href='{0}?{1}'>全部</a>".format(self.get_list_url,self.params.urlencode())) ##等同下面
            # yield mark_safe("<a href=%s?%s>全部</a>" % (self.get_list_url,self.params.urlencode()))  ##等同予 %s
        else:
            ori_nid =None
            yield mark_safe("<a class='active' href='{0}?{1}'>全部</a>".format(self.get_list_url, self.params.urlencode()))
        for obj in self._field:
            if self.is_choince:
                #obj 是元组
                nid = str(obj[0])
                text = str(obj[1])
            else:
                nid = str(obj.pk)
                text = str(obj)
            self.params[self.name] = nid
            if  nid == ori_nid:
                yield mark_safe("<a class='active' href='{0}?{1}'>{2}</a>" .format(self.get_list_url,self.params.urlencode(),text))
            else:
                yield mark_safe("<a  href='{0}?{1}' >{2}</a>" .format(self.get_list_url,self.params.urlencode(),text))

###列表页面类
class GetListView(object):
    """
    用于对列表页面的功能做拆分
    """
    def __init__(self,config,result_list,request):
        """
        :param config: 处理每个表增伤改查功能的对象
        :param result_list: 从数据库查询到的数据
        """
        self.config = config
        self.model_class = config.model_class
        self.request = request
        self.result_list = result_list
        self.search_list = config.search_list
        self.search_value = self.request.GET.get("key","")
        self.action_list = config.action_list
        self.comb_filter  = config.comb_filter


        page_obj=Pagination(self.request,self.result_list)  ##实例化页码对象
        self.page_list = page_obj.page_obj_list()    ##每页的 20对象
        self.page_html=mark_safe(page_obj.bootstrap_page_html())  ##实例化页码导航

        # self.comb_filter = config.comb_filter
        # self.show_add_btn = config.get_show_add_btn()
    def user_online_state(self):
        state=self.request.session.get(settings.PERMISSION_DICT_SESSION_KEY)
        return state
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
        # ['id', 'name', 'email',display_edit,display_del]
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

    def show_comb_search(self):
        """#self.comb_filter  # ['gender','status','dp']
        "gender"，找类中的gender字段对象，并将其对象中的choice获取
        "status"，找类中的status字段对象，并将其对象中的choice获取
        "dp"，找类中的dp字段对象，并将其关联的表中的所有数据获取到
        yield Foo(models.Role.objects.all())
        yield Foo(models.Role.objects.all())
        yield Foo(models.Role.objects.all())
        """

        ###yield  返回到前端
        for name in self.comb_filter:
            _field = self.model_class._meta.get_field(name)
            print(_field,type(_field))
            get_list_url = self.config.get_list_url()
            print(get_list_url)
            if type(_field) == ForeignKey:
                yield FilterRow(_field.rel.to.objects.all(),name,self.request,get_list_url)
            else:
                yield FilterRow(_field.choices,name,self.request,get_list_url,is_choice=True,)

######配置类
class StarkConfig(object):
    """
    初始化类数据
    """
    def __init__(self, model_class):
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
            url(r'^(\d+)/edit/$', self.edit_view, name="%s_%s_edit" % app_model_name),
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

#######通过反向生成获取增删页面的URL ##################
    def get_add_url(self):
        app_model_name = (self.model_class._meta.app_label, self.model_class._meta.model_name,)
        name = "stark:%s_%s_add" % app_model_name
        url_path = reverse(name)
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
    def get_edit_url(self, pk):
        """
        /stark/app01/userinfo/1/
        :param pk:
        :return:
        """
        app_model_name = (self.model_class._meta.app_label, self.model_class._meta.model_name,)
        name = "stark:%s_%s_edit" % app_model_name
        url_path = reverse(name, args=(pk,))
        return url_path
    def get_list_url(self):
        # /stark/app01/userinfo/1/delete/
        # /stark/app02/role/1/delete/
        app_model_name = (self.model_class._meta.app_label, self.model_class._meta.model_name,)
        name = "stark:%s_%s_get_list" % app_model_name
        url_path = reverse(name)
        return url_path

#######处理生成((选择编辑删除)按钮的 url#########
    def display_checkbox(self, is_header=False, row=None):
        if is_header:
            return '选择'
        return mark_safe("<input type='checkbox' name='pk' value='%s' />" % (row.id,))
    def display_edit(self, is_header=False, row=None):
        if is_header:
            return "编辑"
        url_path = self.get_edit_url(pk=row.id)
        return mark_safe('<a href=%s>编辑</a>' % (url_path))
    def display_delete(self, is_header=False, row=None):
        if is_header:
            return '删除'
        url_path = self.get_delete_url(pk=row.id)
        return mark_safe('<a href=%s>删除</a>' % (url_path))

####搜索框关键字搜索 和 组合搜索 函数
    def get_key_search_condtion(self, request):
        key = request.GET.get('key')  # 小偷 -> 构造or条件
        con = Q()
        con.connector = 'OR'
        if key:  ###不为空则添加过滤条件
            for name in self.search_list:
                con.children.append((name, key,))
        return con
    def get_comb_filter_condition(self, request):
        comb_condition = {}
        for name in self.comb_filter:
            val = request.GET.get(name)
            if not val:
                continue
            comb_condition[name] = val
        return comb_condition

#####增删改查页面视图##########
    def get_list_view(self,request):
        ###批量执行某一功能
        if request.method == "POST":
            action = request.POST.get('action')
            print(action,"action")
            func_name = getattr(self,action,None)
            if func_name:
                response = func_name(request,action)
                if response:
                    return response

        result_list = self.model_class.objects.filter(self.get_key_search_condtion(request)).filter(**self.get_comb_filter_condition(request))
        cl = GetListView(self,result_list,request)
        print(bool(cl.user_online_state),"状态####")
        return render(request, "get_list_view.html", {"cl":cl})
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
    def edit_view(self,request,nid):
        obj = self.model_class.objects.filter(pk=nid).first()
        if not obj:
            return HttpResponse('别闹')

        model_form_cls = self.get_model_form_cls()
        if request.method == "GET":
            form = model_form_cls(instance=obj)
            return render(request, 'edit_view.html', {'form': form})
        else:
            form = model_form_cls(instance=obj, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect(self.get_list_url())
            return render(request, 'edit_view.html', {'form': form})
    def delete_view(self,request,nid):
        self.model_class.objects.filter(id=nid).delete()
        return redirect(self.get_list_url())

####### 控制显示列表  整合stark 字符串 和 函数 display 方法##########
    search_list = []
    action_list = []
    list_display = []
    comb_filter = []
    def get_list_display(self):
        result = []
        if self.list_display:
            result.extend(self.list_display)
            result.insert(0, StarkConfig.display_checkbox)
            result.append(StarkConfig.display_edit)
            result.append(StarkConfig.display_delete)
        return result

###注册数据库url
class StarkSite(object):
    """
    注册所有表的 url
    """
    def __init__(self):
        self._registry={}

    def registry(self,model_class,config_cls=None):
        if not  config_cls:
            config_cls = StarkConfig       ###默认是StarkConfig
        self._registry[model_class] = config_cls(model_class)
        # print(self._registry,"打印字典k") ###打印注册到字典 _registry的类
        # print(self._registry.items(),"打印字典v")
    def update_db(self):
        print("#########")

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
        # /admin/app01/userinfo/1/edit/   修改页面
        # /admin/app01/userinfo/1/delete/   删除页面


        /stark/   ->  ([
                            /login/
                            /app01/userinfo/  --> ([
                                                        /                    查看列表
                                                        add/                 添加
                                                        (\d+)/edit/        修改
                                                        (\d+)/delete/        删除
                                                    ])
                            /app01/role/
                                                --> ([
                                                        /                   查看列表
                                                        add/                添加
                                                        (\d+)/edit/        修改
                                                        (\d+)/delete/        删除
                                                    ])
                        ])

        """
        return self.get_urls(), None,"stark"

    def login(self, request):
        return HttpResponse('登录页面')

###单例模式只生成一次
site = StarkSite()


