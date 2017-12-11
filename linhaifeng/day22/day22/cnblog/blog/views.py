from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from django.contrib import auth
from .models import *


def login(request):
    if request.is_ajax():
        username=request.GET.get("username")
        password=request.GET.get("password")
        valid=request.GET.get("valid")
        keep_valid=request.session.get("valid_code")

        '''
        sessionId=request.COOKIE["sessionId"]   # asdsa234asd3sad

        in session表：
        qqqqq=models.sesison.objects.filter(sessionId=asdsa234asd3sad).values("valid_code")

        '''

        loginResponse={"user":None,"error_msg":None}
        if valid.upper() == keep_valid.upper():
            user=auth.authenticate(username=username,password=password)
            if user:
                loginResponse["user"]=username
                auth.login(request,user)

            else:
                loginResponse["error_msg"]="username or password error"
        else:
            loginResponse["error_msg"]="valid error"

        import json

        return HttpResponse(json.dumps(loginResponse))

    return render(request,"login.html")


def get_valid_img(request):

    # 第一步
    # with open("lufei.jpg","rb") as f :
    #     data=f.read()


    # 第二步：
    import PIL
    # from PIL import Image
    # img = Image.new(mode='RGB', size=(120, 30), color=(123, 222, 255))
    # f=open('a.png','wb')
    # img.save(f,"png")
    #
    # f=open("a.png","rb")
    # data=f.read()

    # 第三步：

    # from io import BytesIO
    # f=BytesIO()
    #
    # from PIL import Image
    # img = Image.new(mode='RGB', size=(120, 30), color=(0, 255, 0))
    # img.save(f,"png")
    # data=f.getvalue()
    # return HttpResponse(data)

    # 第四步：

    from io import BytesIO
    f=BytesIO()
    from PIL import Image,ImageDraw,ImageFont
    #
    # # 画字
    # img = Image.new(mode='RGB', size=(120, 30), color=(0, 255, 0))
    # draw = ImageDraw.Draw(img, mode='RGB')
    # font=ImageFont.truetype("blog/static/dist/fonts/kumo.ttf",28)
    # draw.text([15,2],'y',"red",font=font)
    #
    # img.save(f,"png")
    # data=f.getvalue()

    # 第五步：
    import random
    img = Image.new(mode='RGB', size=(120, 30),
                    color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    draw = ImageDraw.Draw(img, mode='RGB')

    char_list=[]
    # 画字
    for i in range(5):
        char = random.choice([chr(random.randint(65, 90)), str(random.randint(1, 9)),chr(random.randint(97, 122)),])

        font = ImageFont.truetype("blog/static/dist/fonts/kumo.ttf", 28)
        draw.text([i * 24, 0], char, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),


                  font=font)

        char_list.append(char)

    #=========================
    # width = 120
    # height = 30
    # def rndColor():
    #     """
    #     生成随机颜色
    #     :return:
    #     """
    #     return (random.randint(0, 255), random.randint(10, 255), random.randint(64, 255))
    # # 写干扰点
    # for i in range(40):
    #     draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())
    #
    # # 写干扰圆圈
    # for i in range(40):
    #     draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())
    #     x = random.randint(0, width)
    #     y = random.randint(0, height)
    #     draw.arc((x, y, x + 4, y + 4), 0, 90, fill=rndColor())
    #
    # # 画干扰线
    # for i in range(5):
    #     x1 = random.randint(0, width)
    #     y1 = random.randint(0, height)
    #     x2 = random.randint(0, width)
    #     y2 = random.randint(0, height)
    #
    #     draw.line((x1, y1, x2, y2), fill=rndColor())


    img.save(f,"png")
    data=f.getvalue()

    s=''.join(char_list)

    request.session["valid_code"]=s

    '''
    Dajngo:
    set_cookie("sessionId","asdsa234asd3sad")
    in session表
    sessionkey           sessiondata
    asdsa234asd3sad      {"valid_code":"qqqqq"}
    '''
    return HttpResponse(data)

import json
from blog.forms import RegForm
from blog import models
def reg(request):

    if request.is_ajax():
        regForm=RegForm(request.POST)

        regResponse={"user":None,"error_msg":None}
        if regForm.is_valid():
            username=regForm.cleaned_data.get("username")
            password=regForm.cleaned_data.get("password")
            email=regForm.cleaned_data.get("email")
            avatar=request.FILES.get("avatar")
            print(regForm.cleaned_data,"------")
            user=UserInfo.objects.create_user(username=username,password=password,email=email,avatar=avatar)
            regResponse["user"]=user.username

        else:
            regResponse["error_msg"]=regForm.errors  # errors只存错误字段
        return HttpResponse(json.dumps(regResponse))

    regForm=RegForm()

    return render(request,'reg.html',locals())

def index(request):

    if not request.user.is_authenticated():
        return redirect("/login/")

    print(request.user.username,"======")
    article_list=models.Article.objects.all()
    return render(request,"index.html",{"article_list":article_list})


def logout(request):
    auth.logout(request)
    
    return redirect("/login/")


def homeSite(request,username,**kwargs):
    print(kwargs,"=====")
    # 查询当前的用户对象
    user=UserInfo.objects.get(username=username)
   # 查询当前站点对象
    blog=user.blog


    # 查询当前站点所有的文章
    if not kwargs:
        article_list=Article.objects.filter(user__username=username).order_by("-create_time")
    else:
        if kwargs.get("condition")=="category":
            para=kwargs.get("para")
            print(kwargs)
            article_list=Article.objects.filter(user__username=username).filter(homeCategory__title=para)
        elif kwargs.get("condition")=="tag":pass
        else:pass
    # 查询当前站点的所有分类名称
    #方式1：
    cateList=models.HomeCategory.objects.filter(blog=blog)

    #方式2： 查询每一个分类名称以及对应的文章个数
    from django.db.models import Count,Sum,Min
    # cate_list=models.HomeCategory.objects.filter(blog=blog).annotate(c=Count("article__nid")).values_list("title","c")
    # print(cate_list) # <QuerySet [('yuan的python', 2), ('yuan的数据库', 1)]>


    ########################
    # 查询当前站点所有标签的名称以及对应的文章数
    tagList=models.Tag.objects.filter(blog=blog)

    #
    dateList=models.Article.objects.filter(user=user).extra(select={"formatDate":"strftime('%%Y-%%m',create_time)"}).values_list("formatDate").annotate(Count("nid"))
    # print(dateList)
    return render(request,"homeSite.html",locals())


def articleDetail(request,username,article_id):
    # 查询当前的用户对象
    user = UserInfo.objects.get(username=username)
    # 查询当前站点对象
    blog = user.blog

    # 查询当前站点的所有分类名称
    # 方式1：
    cateList = models.HomeCategory.objects.filter(blog=blog)

    # 方式2： 查询每一个分类名称以及对应的文章个数
    from django.db.models import Count, Sum, Min
    # cate_list=models.HomeCategory.objects.filter(blog=blog).annotate(c=Count("article__nid")).values_list("title","c")
    # print(cate_list) # <QuerySet [('yuan的python', 2), ('yuan的数据库', 1)]>


    ########################
    # 查询当前站点所有标签的名称以及对应的文章数
    tagList = models.Tag.objects.filter(blog=blog)

    #
    dateList = models.Article.objects.filter(user=user).extra(
        select={"formatDate": "strftime('%%Y-%%m',create_time)"}).values_list("formatDate").annotate(Count("nid"))
    # print(dateList)

    #####################################################
    article_obj=models.Article.objects.filter(nid=article_id).first()
    print(article_obj,"00000")

    return render(request,"articleDetail.html",locals())


def diggit(request):
    from django.db.models import F
    from django.db import transaction
    state={"state":False}
    try:
        user_id=request.user.nid
        article_id=request.POST.get("article_id")
        with transaction.atomic():
            models.ArticleUpDown.objects.create(user_id=user_id,article_id=article_id)
            models.Article.objects.filter(nid=article_id).update(up_count=F("up_count")+1)
        state = {"state": True}
    except:
        pass


    from django.http import JsonResponse
    return JsonResponse(state)