from django.db import models

# Create your models here.

class Book(models.Model):

    nid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=32)
    pubDate=models.DateField()
    price=models.DecimalField(max_digits=6,decimal_places=2)



    publisher=models.ForeignKey(to="Publish")

class Publish(models.Model):
    name=models.CharField(max_length=32)
    addr=models.CharField(max_length=32)
    tel=models.BigIntegerField()


