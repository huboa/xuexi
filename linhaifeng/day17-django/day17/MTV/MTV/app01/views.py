from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from MTV import settings

def login(request):
    # print("method",request.method)
    # print("path",request.path)
    #
    # print("COOKIES",request.COOKIES)
    # print("full_path",request.get_full_path())   # /login/?a=1&b=2


    if request.method=="POST":

        print("GET",request.GET)
        print("POST",request.POST)
        user=request.POST.get("user")
        pwd=request.POST.get("pwd")
        # hobby=request.POST.getlist("hobby")
        # hobby=request.POST.getlist("pro")
        # print("hobby",hobby)

        if user=="yuan" and pwd=="123":
            #return HttpResponse("登录成功！")


            #return redirect("/index/")
            s = "egon"

            age = 12
            return render(request,"index.html",{"name":s,"age":age})

        else:
            redirect("/login/")


    print("GET...", request.GET)
    print("POST..", request.POST)
    return render(request,"login.html")

def index(request):

    s="egon"

    age=12

    l=[111,222,333]
    l=[]

    d={"name":"yuan","age":32}

    a_ele="<a href=''>点击</a>"
    import datetime

    date=datetime.datetime.now()
    # import os
    #
    # path=os.path.join(settings.BASE_DIR,"templates","index.html")
    # with open(path) as f:
    #     data=f.read()
    #
    # data=data%s
    # return HttpResponse(data)

    class Person(object):

        def __init__(self,name,age):
            self.name=name
            self.age=age

        def dream(self):

            return "dreaming....."

    alex=Person("alex",34)
    egon=Person("egon",35)
    alvin=Person("alvin",34)

    personList=[alex,egon,alvin]

    #return render(request,"index.html",{"name":s,"age":age,"l":l,"d":d,"date":date,"personList":personList})
    return render(request,"index.html",locals())



















