from django.http import QueryDict

params = QueryDict(mutable=True,encoding='utf-8')

params['k1'] = 'v1'

print(params)


