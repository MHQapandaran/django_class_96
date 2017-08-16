from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Book, Borrow

from django.contrib.auth.decorators import login_required

from django.db.models import Q

# Create your views here.

def staff_decorator(function):
    @login_required
    def f2(request):
        if request.user.user.role == 0:
            return function(request)
        else:
            return HttpResponse("You do not have the required access level")
    return f2

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
    
@login_required
def reserve(request):
    
    id = request.GET['id']
    
    book = get_object_or_404(Book, id=id)

    borrow = Borrow.objects.filter(book = book).last()
    
    if borrow is not None and borrow.end is None:
        return HttpResponse("The book is not available ")
    
    borrow = Borrow.objects.filter( user = request.user.user).last()
    
    if borrow is not None and borrow.end is None:
        return HttpResponse("You have not returned your last book")
    
    b = Borrow()
    
    b.user = request.user.user
    b.book = book
    b.save()
    
    return HttpResponse("OK")
    pass



