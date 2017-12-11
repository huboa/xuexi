from django.db import models

# Create your models here.

class Book(models.Model):

    nid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=32)
    pubDate=models.DateField()
    price=models.DecimalField(max_digits=6,decimal_places=2)

    read_num=models.IntegerField(default=0)
    comment_num=models.IntegerField(default=0)
    # 书籍与出版社： 一对多
    publisher=models.ForeignKey(to="Publish",related_name="bookList")

    # 书籍与作者： 多对多
    authors=models.ManyToManyField("Author")

    def __str__(self):
        return self.title

class Publish(models.Model):
    name=models.CharField(max_length=32)
    addr=models.CharField(max_length=32)
    tel=models.BigIntegerField()


class Author(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    tel=models.CharField(max_length=32)

    def __str__(self):
        return self.name+" "+str(self.age)


class AuthorDetail(models.Model):

    addr=models.CharField(max_length=32)
    author=models.OneToOneField("Author")




