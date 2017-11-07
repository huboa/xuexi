from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from app01 import models


def index(request):


    # 查询所有的书籍
    bookList=models.Book.objects.all() # 返回值QuerySet    [obj1,obj2....]


    return render(request,"index.html",{"bookList":bookList})



def add(request):

    if request.method=="POST":
        print(request.POST)
        title=request.POST.get("title")
        pubdate=request.POST.get("pubdate")
        price=request.POST.get("price")
        publish=request.POST.get("publish")

        # 插入数据
        models.Book.objects.create(title=title,pubDate=pubdate,price=price,publish=publish)

        return redirect("/index/")
    return render(request,"add.html")


def delBook(request,id):

    models.Book.objects.filter(id=id).delete()

    return redirect("/index/")

def editBook(request,id):
    # if request.method=="POST":
    #
    #     models.Book.objects.filter(id=id).update()
    #     return redirect("/index/")

    edit_book=models.Book.objects.filter(id=id)[0]      # 返回值QuerySet    [obj1,]
    return render(request,"edit.html",{"edit_book":edit_book})