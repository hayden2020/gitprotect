

from django.http import HttpResponse

def index(request):
    html="<h1>这是主页</h1>"
    return HttpResponse(html)

def page_view(request):
    html="<h1>HELLO world</h1>"
    return HttpResponse(html)

def pagen_view(request,n):
    html="<h1>这是第%s个页面</h1>" % n
    return HttpResponse(html)

def person_view(request, name=None,age=None):
    s="xingming:"+name
    s+="nianlin:"+age
    return HttpResponse(s)