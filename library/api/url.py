from django.conf.urls import url

from . import views

urlpatterns = [
   #url(r'^books/$', views.book_list, name='book_list'),
   url(r'^books/$', views.BookList.as_view(), name='book_list'),
]
