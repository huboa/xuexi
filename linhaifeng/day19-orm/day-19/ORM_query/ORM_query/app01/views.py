from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from app01 import models


def index(request):
    book_list=models.Book.objects.all()


    return render(request,"index.html",{"book_list":book_list})


def add(request):

    if request.method=="POST":
        title = request.POST.get("title")
        pubdate = request.POST.get("pubdate")
        price = request.POST.get("price")
        publish_id = request.POST.get("pub")
        author_id_list=request.POST.getlist("author_id_list") # [1,3]

        book_obj=models.Book.objects.create(title=title,pubDate=pubdate,price=price,publisher_id=publish_id)
        authorList=models.Author.objects.filter(id__in=author_id_list)

        #book_obj.authors.add(*authorList)
        # book_obj.authors.add(*author_id_list) #########################another way

        ####################################一对多的添加

        # # 一对多 添加数据 方式1
        # # publish_obj=models.Publish.objects.get(name="renmin")
        # # book_obj=models.Book.objects.create(title="python",price=122,pubDate="2012-12-12",publisher=publish_obj)
        #
        # # 一对多 添加数据 方式2
        # book_obj=models.Book.objects.create(title=titles,price=price,pubDate=pubdate,publisher_id=publish_id)
        # print(book_obj.title)
        #
        # # obj=models.Book(title="python",price=122,pubDate="2012-12-12",publisher=publish_obj)
        # # obj.save()


        ####################################多对多的添加###################

        # book_obj=models.Book.objects.create(title=title,pubDate=pubdate,price=price,publisher_id=publish_id)
        # 绑定作者关系： alex，egon


        # 不能直接在第三张表中插入记录，因为没有第三张表名
        # alex_id=models.Author.objects.get(name="alex").id
        # egon_id=models.Author.objects.get(name="egon").id
        #
        # book_authors.objects.create(book_id=book_obj.id,author_id=alex_id)
        # book_authors.objects.create(book_id=book_obj.id,author_id=egon_id)

        # authors字段

        # 绑定关系
        # print(book_obj.authors.all(),"11111")   #  <QuerySet []>
        #
        # # alex=models.Author.objects.get(name="alex")
        # # egon=models.Author.objects.get(name="egon")
        #
        # author_list=models.Author.objects.all()
        #
        # book_obj.authors.add(*author_list)
        #
        # print(book_obj.authors.all(),"2222")     # <QuerySet [<Author: Author object>, <Author: Author object>]>

        # 解除关系
        # book_obj=models.Book.objects.get(nid=13)
        # print(book_obj.authors.all())
        # # alex=models.Author.objects.get(name='alex')
        # # book_obj.authors.remove(alex)
        #
        # # author_list = models.Author.objects.filter(id__gt=1)
        # # book_obj.authors.remove(*author_list)
        #
        # # 清空
        # book_obj.authors.clear()


        return redirect("/index/")



    publish_list=models.Publish.objects.all()
    author_list=models.Author.objects.all()

    return render(request,"add.html",{"publish_list":publish_list,"author_list":author_list})



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


    ###########################################一对多查询########################

    # 正向查询： 按字段

    # 查询 python这本书的出版社的名称和地址

    # book_python=models.Book.objects.filter(title="python").first()
    #
    # print(book_python.title)
    # print(book_python.price)
    #
    # print(book_python.publisher) # Publish object : 与这本书关联的出版社的对象
    # print(book_python.publisher.name)
    # print(book_python.publisher.addr)

    # 反向查询：按关联的表名（小写）_set

    # 查询人民出版社出版过的所有书籍名称及价格

    # pub_obj=models.Publish.objects.get(name="renmin")
    # book_list=pub_obj.book_set.all()   # QuerySet 与这个出版社关联的所有书籍对象
    #
    # for obj in book_list:
    #     print(obj.title,obj.price)


    ###########################################一对一查询########################

    # 正向查询： 按字段

    # 查询addr在沙河的作者
    # authorDetail=models.AuthorDetail.objects.get(addr="shahe")
    # print(authorDetail.author.name) # alex
    #
    #
    # # 反向查询：按 表名（小写）
    #
    # # 查询 alex混迹在哪里
    #
    # alex=models.Author.objects.get(name="alex")
    # print(alex.authordetail.addr) # shahe

    ###########################################多对多查询########################


    # 多对多的正向 查询： 按字段

    # 查询 python这本书的所有作者的姓名和年龄

    # book_python=models.Book.objects.get(title="python")
    # author_list=book_python.authors.all()
    # for obj in author_list:
    #     print(obj.name,obj.age)
    #
    # book_pythons = models.Book.objects.filter(title="python")
    # for book_python in book_pythons:
    #     author_list = book_python.authors.all()
    #     for obj in author_list:
    #         print(obj.name, obj.age)


    # 多对多的反向查询  按关联的表名（小写）_set

    # alex出版过的所有书籍的明显名称

    # alex=models.Author.objects.get(name="alex")
    # book_list=alex.book_set.all()
    # for i in book_list:
    #     print(i.title,i.price)





    ###########>>>>>>>>>>>>>>>>>>>>>>基于双下划线
    # 查询 python这本书的价格
    # ret=models.Book.objects.filter(title="python").values("price","title")
    # print(ret) # <QuerySet [{'price': Decimal('122.00')}]>


    #查询python这本书的出版社的名称和地址

    #正向查询  按字段    基于book表
    # ret2=models.Book.objects.filter(title="python").values_list("publisher__name")
    # print(ret2)
    #
    # # 反向查询 按表名  if 设置了related_name: 按设置值
    ret3=models.Publish.objects.filter(bookList__title="python").values_list("name")
    print(ret3)

    # 查询人民出版社出版过的所有书籍名称及价格

    # ret4=models.Book.objects.filter(publisher__name="renmin").values("title","price")
    # print(ret4.count())

    # ret5=models.Publish.objects.filter(name="renmin").values("bookList__title","bookList__price")
    # print(ret5.count())

    #查询egon出过的所有书籍的名字(多对多)

    # ret6=models.Author.objects.filter(name="egon").values_list("book__title")
    # print(ret6)

    # ret7=models.Book.objects.filter(authors__name__contains="eg").values("title")
    # print(ret7)

    # 地址以沙河开头的的作者出版过的所有书籍名称以及出版社名称
    # ret8=models.Book.objects.filter(authors__authordetail__addr__startswith="sha").values("title","publisher__name")
    # print(ret8)








    return HttpResponse("OK")



def edit(request,id):


    publish_list = models.Publish.objects.all()
    author_list = models.Author.objects.all()
    edit_book=models.Book.objects.get(nid=id)
    return render(request,"edit.html",locals())



def juheQuery(reqeuest):
     from django.db.models import Avg,Count,Sum,Min,Max
     # 单纯聚合函数
     # 计算所有图书的平均价格
     # ret=models.Book.objects.all().aggregate(priceSum=Sum("price"))
     # print(ret)  # {'priceSum': Decimal('2158.00')}

     # 统计每一本书的作者个数

     # ret2=models.Book.objects.all().annotate(authors_num=Count("authors"))  # QuerySet
     # print(ret2)   # [book_obj1,book_obj2,book_obj3,book_obj4,....]
     #
     # for obj in ret2:
     #     print(obj.nid,obj.title,obj.authors_num)


     # 查询每一个出版社出版过的所有书籍的总价格

      #方式1：
     # ret3=models.Publish.objects.all().annotate(priceSum=Sum("bookList__price"))
     #
     # for obj in ret3:
     #     print(obj.id,obj.name,obj.priceSum)

     # ret4 = models.Publish.objects.all().annotate(priceSum=Sum("bookList__price")).values("name","priceSum")
     # print(ret4)

     # 方式2：
     # ret5=models.Book.objects.all().values("publisher__name").annotate(priceSum=Sum("price")).values("publisher__name","priceSum")
     # print(ret5)





     return HttpResponse("OK")




def FQQuery(request):

    from django.db.models import F,Q


    ###################################F查询

    # ret1=models.Book.objects.filter(comment_num__gt=50)
    # ret2=models.Book.objects.filter(comment_num__gt=F("read_num")*2)
    # print(ret2)

    #models.Book.objects.all().update(price=F("price")+10)

    ################################## Q查询
    ret3=models.Book.objects.filter(comment_num__gt=50,read_num__gt=50)
    ret3=models.Book.objects.filter(Q(comment_num__gt=100)|Q(read_num__gt=100))
    print(ret3)

    #注意事项
    #ret3=models.Book.objects.filter(price__lt=100,(Q(comment_num__gt=100)|Q(read_num__gt=100)))

    return HttpResponse("OK")
