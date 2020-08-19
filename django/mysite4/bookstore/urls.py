# file: bookstore/urls.py

from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^add',views.add_view),
    url(r'^all',views.show_all),  # all 表示网页地址
    url(r'^mod/(\d+)',views.mod_view),
    url(r'^del/(\d+)',views.del_view),

]