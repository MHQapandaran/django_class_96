from django.conf.urls import url

from . import views

app_name="base"
urlpatterns = [
   url(r'^$', views.hello_world, name='hello_world'),
   url(r'^books/$', views.list_books, name='list_books'),
   url(r'^book/$', views.get_book, name='get_book'),
   url(r'^book_search/$', views.search_book, name='search_book'),
   url(r'^reserve/$', views.reserve, name='reserve'),
]
