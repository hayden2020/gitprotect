from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=30,db_index=True,) # 等于varchar(30)
    #price=models.DecimalField(decimal_places=2,
     #                         max_digits=7)  # 等于 Decimal(7，2)
    pub = models.CharField(max_length=50, verbose_name='出版社', null=True, )
    price = models.DecimalField(decimal_places=2, max_digits=7,
                                default=999, verbose_name='定价')
    market_price = models.DecimalField(max_digits=7,
                                       decimal_places=2,
                                       verbose_name='零售价',
                                       default=88, )  # 等于 Decimal(7，2)


class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(verbose_name='年龄')  # IntegerField 姓名非空
    email = models.EmailField(verbose_name='邮箱')  # 邮箱允许