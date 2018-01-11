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
    def proceess_request(self,request):
        #当前访问的URL
        current_url = request.path_info
        print(current_url,"rbac.py")
        if current_url == '/login/':
            return HttpResponse('当前用户无权限信息')
        #当前用户的所有权限
        permision_dic = request.seesion.get(settings.PERMISSIONS_DICT_SESSION_KEY)
        # print(permision_dic)
        # print(current_url)
        tag=False
        for item in permision_dic:
            urls = item["urls"]
            codes = item["codes"]
            print(urls)
            for rex in urls:
                if re.match(rex,current_url):
                    tag = True
                    request.permission_codes = codes
                    break
            if tag:
                break


        if not tag:
            return  HttpResponse('当前用户无权限信息')

