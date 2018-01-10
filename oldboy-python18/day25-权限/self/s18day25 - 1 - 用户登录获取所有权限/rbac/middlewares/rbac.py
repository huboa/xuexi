from django.conf import settings

class RbacMiddleware(object):
    def proceess_request(self,request):
        permision_dic = request.seesion.get(settings.PERMISSIONS_DICT_SESSION_KEY)
        print(permision_dic)