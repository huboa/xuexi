from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


def index(request):
    if not request.COOKIES.get("is_login"):
        return redirect("/login/")


    return render(request,"index.html")


def ajax_send(request):

    print(request.body)   # b'name=yuan&pwd=123'
    print(request.POST)   # <QueryDict: {'name': ['yuan'], 'pwd': ['123']}>
    print(request.GET)

    s=request.body.decode("utf8")
    import json
    d=json.loads(s)
    print(d["name"])


    return HttpResponse("OK")


def back(request):

    return HttpResponse("OK")

def login(request):
    if request.method=="POST":
        user=request.POST.get("user")
        pwd=request.POST.get("pwd")

        if user=="alex" and pwd=="123":
            obj=redirect("/index/")
            obj.set_cookie("is_login",True,max_age=20)
            obj.set_cookie("username",user)
            return obj

    return render(request,"login.html")


from app01 import forms



def reg(request):

    if request.method=="POST":
        # print(request.POST)
        regForm=forms.RegForm(request.POST)

        if regForm.is_valid():  #  当所有的字段都验证通过的时候返回True
            print(1111)
            print(regForm.cleaned_data)     #  字典  存放的是所有的干净数据   {"username":"yuanasd",.....}
            # 存放数据库
        else:

            pass
            # print("errors",regForm.errors.get("username"))  # 字典  存放的错误字典   {"username":["长度不够"]，"email":["格式错误"]]
            # print("errors",type(regForm.errors.get("username")))  # 字典  存放的错误字典   {"username":["长度不够"]，"email":["格式错误"]]
            #
            # print("cleaned_data",regForm.cleaned_data)

        return render(request, "reg.html", {"regForm": regForm})

    regForm = forms.RegForm()
    return render(request,"reg.html",{"regForm":regForm})