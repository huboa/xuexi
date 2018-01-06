from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from app01 import models


def index(request):


    # 查询所有的书籍
    bookList=models.Book.objects.all() # 返回值QuerySet    [obj1,obj2....]

    #return redirect("/index/")
    return render(request,"new_index.html",{"bookList":bookList})


def add(request):


    if request.method=="POST":
        print(request.POST)
        title=request.POST.get("title")
        pubdate=request.POST.get("pubdate")
        price=request.POST.get("price")
        publish=request.POST.get("publish")

        # 插入数据方式1,create有返回值：插入的记录对象：
        # book_obj=models.Book.objects.create(title=title,pubDate=pubdate,price=price,publish=publish)
        # print(book_obj.title)
        # print(book_obj.price)
        # 插入数据方式2：
        book_obj=models.Book(title=title,pubDate=pubdate,publish=publish)
        book_obj.price=price
        book_obj.save()

        return redirect("/index/")

    return render(request,"add2.html")


def delBook(request,id):

    models.Book.objects.filter(id=id).delete()

    return redirect("/index/")



def editBook(request,id):
    if request.method=="POST":

        #方式1：
        titles = request.POST.get("title")
        pubdate = request.POST.get("pubdate")
        price = request.POST.get("price")
        publish = request.POST.get("publish")

        models.Book.objects.filter(id=id).update(title=titles,publish=publish,price=price,pubDate=pubdate)

        # # 方式2：
        # print(request.POST.dict(),"=====")
        #
        # models.Book.objects.filter(id=id).update(**request.POST.dict())
        #
        # return redirect("/index/")

    edit_book=models.Book.objects.filter(id=id)[0]      # 返回值QuerySet    [obj1,]
    return render(request,"edit.html",{"edit_book":edit_book})

def temp(request):

    if request.method=="POST":
        return HttpResponse("OK")
    n=10

    return render(request,"temp.html",locals())


def query(request):
    #  查询API

    # 1 all()
    # book_list=models.Book.objects.all() # QuerySet  [obj1，obj2,]
    #
    # print(book_list[2].title)
    # for book_obj in book_list:
    #     print(book_obj.title)

    # 2 filter(**kwargs) # QuerySet  [obj1，obj2,]

    #book_list=models.Book.objects.filter(price=134)
    #book_list=models.Book.objects.filter(id=11)  #[obj1,]
    # from django.db.models import Q
    # book_list=models.Book.objects.filter(Q(price=134)|Q(title='语文书'))
    #
    #
    # for book_obj in book_list:
    #     print(book_obj.title)

    # 3 get(**kwargs)方法  # model对象  返回结果有且只能有一个

    #book_obj=models.Book.objects.get(title="数学书2")
    #book_obj=models.Book.objects.get(price=134)
    # book_obj=models.Book.objects.get(id=11)
    # print(book_obj.title)

    # 4 first()  last()

    # book_obj=models.Book.objects.all().first()
    # print(book_obj.title)
    #
    # book_obj=models.Book.objects.filter(price=134).last()

    # 5 exclude 刷选出不符合条件的QuerySet

    # book_list=models.Book.objects.exclude(price=134)  # QuerySet  [obj1，obj2,]
    # for book in book_list:
    #     print(book.title)

    # 6 count
    # count = models.Book.objects.filter(price=134).count()
    # print(count)

    # 7order_by(*field)

    # book_list=models.Book.objects.all().order_by("-price").reverse()
    # for i in book_list:
    #     print(i.title,i.price)

    # values
    # ret=models.Book.objects.all().values("title",'price') # # QuerySet  [{}，{},{},{}]
    # print(ret) # <QuerySet [{'title': '语文书'}, {'title': '数学书'}, {'title': '英语书'}, {'title': '物理书'}]>

    # values_list
    # ret = models.Book.objects.all().values_list("title")
    # print(ret) # <QuerySet [('语文书',), ('数学书',), ('英语书',), ('物理书',)]>


    # exist
    # ret=models.Book.objects.all().exists()
    #
    # if ret:
    #     print("Ok")
    # else:
    #     print("NO")

    #===========================完美的双下划线================================

    # # book_list=models.Book.objects.filter(id__gt=10)
    # # print(book_list.count())
    #
    # book_list=models.Book.objects.filter(title__startswith="语")
    # book_list=models.Book.objects.filter(title__icontains="py")
    # print(book_list[0].title)






    return HttpResponse("OK")