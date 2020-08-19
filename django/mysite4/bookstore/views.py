# file: bookstore/views.py

from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.http import HttpResponseRedirect  # 重定向
# Create your views here.

# file:bookstore/views.py

# def add_view(request):
#     try:
#         # 方法1
#         # abook=models.Book.objects.create(
#         #     title='Python',price=68)
#         # 方法2
#         abook=models.Book(price=98)
#         abook.title='西游记'
#         abook.save()  # 真正执行SQL语句
#         return HttpResponse("添加图书成功")
#     except Exception as err:
#         return HttpResponse("添加图书失败")

def add_view(request):
    if request.method=='GET':
        return render(request,'bookstore/add_book.html')
    elif request.method=='POST':
        title=request.POST.get('title')
        pub=request.POST.get('pub')
        price=request.POST.get('price')
        market_price=request.POST.get('market_price')
    try:
        models.Book.objects.create(
            title=title,
            pub=pub,
            price=price,
            market_price=market_price
        )
        return HttpResponseRedirect('/bookstore/all')
    except:
        return HttpResponse("添加失败")

def show_all(request):
    books=models.Book.objects.all()  # 查询所有的图书
    #books = models.Book.objects.filter(price__range=(50,80))  # 查询50到80的价格
    #books = models.Book.objects.filter(price__lte=80)
    # for abook in books:
    #     print("书名"+abook.title)
    # return HttpResponse("查询成功")

    return render(request,'bookstore/list.html',locals())

def mod_view(request,id):
    try:
        abook=models.Book.objects.get(id=id)
    except :
         return HttpResponse("没有id为" + id +"的数据记录")
    if request.method=='GET':
        return render(request,'bookstore/mod.html',locals())
    elif request.method=='POST':
        market_price=float(request.POST.get('market_price',))  #
        abook.market_price=market_price   # 修改字段的值
        abook.save()
        return HttpResponseRedirect('/bookstore/all')  # 修改成功后u返回指定 的页面

def del_view(request,id):
    try:
        abook=models.Book.objects.get(id=id)
    except Exception as err:
        return HttpResponse("删除失败")
    abook.delete()
    return HttpResponseRedirect('/bookstore/all')