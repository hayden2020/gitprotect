
from django.http import HttpResponse
from django.shortcuts import render
def sum_view(request):
    if request.method=='GET':
        try :
            # http:127.0.0.1:8000/sum?start=1&stop=101&step=1
            start=request.GET.get('start','0')
            start=int(start)
            stop=request.GET['stop']
            stop=int(stop)
            step=request.GET.get('step','1')
            step=int(step)
            mysum=sum(range(start,stop,step))
            html='和是：%d' %mysum
            return HttpResponse(html)
        except Exception as err:
            return HttpResponse("您给的查询字符无效")


login_form_html='''
<form action="/login" method="post">
   用户名：<input name="username" type="text">
   <input type="submit" value="登陆">


</form>
'''
def login_view(request):
    if request.method=='GET':
        return HttpResponse(login_form_html)
    elif request.method=='POST':
        name=request.POST.get('username','属性错误')
        html="姓名："+name
        return HttpResponse(html)

def login2_view(request):
    if request.method=='GET':
        #返回模板生成的html 给浏览器
        # 方法1
        #1.先加载模块,让模块生存模板
        # from django.template import loader
        # t=loader.get_template('mylogin.html')
        # #2.用模板生成html
        # html=t.render({"name":'tarena'})
        # #3.将html返回给浏览器
        #return HttpResponse(html)
        #方法2
        from django.shortcuts import render
        return render(request,"mylogin.html",{"name":'老魏'})


def mycal_view(request):
    if request.method=='GET':
        return render(request,'mycal.html')
    elif request.method=='POST':
        x=int(request.POST.get('x','0'))
        y= int(request.POST.get('y','0'))
        op=request.POST.get('op')
        if op=='add':
            result=x+y
        elif op=='sub':
            result=x-y
        elif op=='mul':
             result=x*y
        elif op=='div':
            result=x/y

        return render(request,'mycal.html',locals())

def for_view(request):
    lst=['北京','上海 ','天津']
    return render(request,'for.html',locals())


def index_view(request):
    return render(request,'base.html')

def spor_view(request):
    return render(request,'sport.html')

def new_view(request):
    pass
