import re
from django.conf import settings
from django.shortcuts import HttpResponse

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

class RbacMiddleware(MiddlewareMixin):
    def process_request(self,request):
        #当前访问的URL
        current_url = request.path_info
        print("访问的路径",current_url)
        for valid_url in settings.VALID_LIST:
            print(valid_url,current_url,re.match(valid_url,current_url) )
            if re.match(valid_url,current_url) :
                print("匹配结果")
                return None

        #当前用户的所有权限
        permision_dic = request.session.get(settings.PERMISSIONS_DICT_SESSION_KEY)
        print("中间键0001",permision_dic)

        tag=False
        for item in permision_dic:
            urls = permision_dic[item]["urls"]
            codes = permision_dic[item]['codes']
            # print(urls)
            # #print(codes)
            for rex in urls:
                rex = settings.REX_FORMAT %(rex,)
                if re.match(rex,current_url):
                    tag = True
                    print(urls)
                    request.permission_codes = codes
                    break
            if tag:
                break

        if not tag:
            return  HttpResponse('当前用户无权限信息')

class Row1(MiddlewareMixin):
    def process_request(self,request):
        print("中间件1请求")
    def process_response(self,request,response):
        print("中间件1返回")
        return response
