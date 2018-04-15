"""
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

@Request.application
def hello(request):
    return Response('Hello World!')

if __name__ == '__main__':
    # 当请求打来之后，自动执行：hello()
    run_simple('localhost', 4000, hello)
"""


from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

class Foo(object):
    def __call__(self, *args, **kwargs):
        return Response('Hello World!')

if __name__ == '__main__':
    # 当请求打来之后，自动执行：hello()
    obj = Foo()
    run_simple('localhost', 4000, obj)