from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from app01 import models


def index(request):
    book_list=models.Book.objects.all()
    return render(request,"index.html",{"book_list":book_list})


def add(request):

    if request.method=="POST":
        titles = request.POST.get("title")
        pubdate = request.POST.get("pubdate")
        price = request.POST.get("price")
        publish_id = request.POST.get("pub")




        # 一对多 添加数据 方式1
        # publish_obj=models.Publish.objects.get(name="renmin")
        # book_obj=models.Book.objects.create(title="python",price=122,pubDate="2012-12-12",publisher=publish_obj)

        # 一对多 添加数据 方式2
        book_obj=models.Book.objects.create(title=titles,price=price,pubDate=pubdate,publisher_id=publish_id)
        print(book_obj.title)

        # obj=models.Book(title="python",price=122,pubDate="2012-12-12",publisher=publish_obj)
        # obj.save()
        return redirect("/index/")



    publish_list=models.Publish.objects.all()

    return render(request,"add.html",{"publish_list":publish_list})



    # if request.method=="POST":
    #     titles = request.POST.get("title")
    #     pubdate = request.POST.get("pubdate")
    #     price = request.POST.get("price")
    #     publish_id = request.POST.get("pub")
    #
    #
    #     # 添加一对多的数据方式1:
    #     book_obj=models.Book.objects.create(title=titles,pubDate=pubdate,price=price,publisher_id=publish_id)
    #
    #     # 添加一对多的数据方式2：
    #
    #     publish_obj=models.Publish.objects.filter(name="renmin")[0]
    #     models.Book.objects.create(title=titles, pubDate=pubdate, price=price, publisher=publish_obj)   # publisher：与这本书关联的出版社对象
    #
    #
    #     return redirect("/index/")
    #
    # publish_list=models.Publish.objects.all()
    # return render(request,"add.html",{"publish_list":publish_list})




def query(request):

    # 查询 python这本书的出版社的名称和地址

    book_python=models.Book.objects.filter(title="python").first()

    print(book_python.title)
    print(book_python.price)

    print(book_python.publisher) # Publish object : 与这本书关联的出版社的对象
    print(book_python.publisher.name)
    print(book_python.publisher.addr)

    return HttpResponse("OK")




