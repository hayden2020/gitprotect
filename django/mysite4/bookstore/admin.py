# file:bookstore/admin
from django.contrib import admin

# Register your models here.

from . import models
class BookManager(admin.ModelAdmin):   # 模型管理器类,可以为后台管理添加功能
    list_display = ['id','title','pub','price','market_price']
    list_display_links = ['id','title']
    list_filter = ['pub']
    search_fields = ['title','pub']
    list_editable = ['market_price']
    #list_per_page = ['pub']
class AuthorManager(admin.ModelAdmin):
    list_display=['id','name','age']
    list_display_links = ['id', 'name']
    list_filter = ['name']
    search_fields = ['id', 'name']
class WifeManager(admin.ModelAdmin):
    list_display=['id','name','author']
admin.site.register(models.Book,BookManager)

admin.site.register(models.Author,AuthorManager)
admin.site.register(models.Wife,WifeManager)