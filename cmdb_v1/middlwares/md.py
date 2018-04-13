from django.conf import settings
from django.shortcuts import redirect,HttpResponse

from django.middleware.csrf import CsrfViewMiddleware

####copy 过来的系统的
class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response

###M1
class M1(MiddlewareMixin):

    def process_request(self,request,*args,**kwargs):
        # 如果当前的URL是 /login/ ，那就跳过该中间件的process_request方法
        # /login/?name=xxx
        # /login/
        if request.path_info == '/login/':
            return None

        # 排除/login/以外的所有URL，对用户认证。
        user_info = request.session.get(settings.USER_SESSION_KEY)
        print(user_info,"user_info")
        if not user_info:
            # 未登陆
            return redirect('/login/')

        # 已登陆
    def process_response(self, request, response):
        print('m1.process_response')
        return response

    # def process_view(self, request, callback, callback_args, callback_kwargs):
    #     pass
    #
    # def process_exception(self,request, exception):
    #     # 异常写入日志
    #     # return HttpResponse('服务器出问题了。。。')
    #     pass



###M2
# class M2(MiddlewareMixin):
#     def process_request(self,request,*args,**kwargs):
#         print('m2.process_request')
#
#     def process_response(self, request, response):
#         print('m2.process_response')
#         return response
#
#     def process_template_response(self,request,response):
#         """
#         视图函数返回的对象，其中如有有render方法，则该方法就会被执行
#         :param request:
#         :param response:
#         :return:
#         """
#         return response
