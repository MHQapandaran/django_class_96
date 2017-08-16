from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Book


from django.db.models import Q

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World!")

def list_books(request):
    list_book = Book.objects.all()
    
    return render(request, 'lib_base_model/book_list.html', {"book_list": list_book})

def get_book(request):
    id = request.GET['id']
    
    book = get_object_or_404(Book, id=id)
    return render(request, 'lib_base_model/book.html', {"book": book})
        

def search_book(request):
    query = request.GET['q']
    
    list_book = Book.objects.filter(name__contains=query) | Book.objects.filter(summary__contains=query)
    
    return render(request, 'lib_base_model/book_list.html', {"book_list": list_book})
    

def reserve(request):
    pass
