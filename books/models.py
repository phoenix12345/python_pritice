from django.db import models

# Create your models here.

#以下的每个数据模型都是django.db.models.Model的子类,父类Model包含了所有和数据库打交道的方法
#每个模型相当于单个数据库表，每个属性也是这个表中的一个字段，属性名就是字段名
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    countray = models.CharField(max_length=50)
    website = models.URLField()

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    headshot = models.ImageField(upload_to='tmp')

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,)
    publication_date = models.DateField()
