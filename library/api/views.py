from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from lib_base_model.models import Book
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from rest_framework import generics, mixins
from django.http import HttpResponse
# Create your views here.

class BookList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        if request.auth is not None and request.user.user.role == 1:
            return self.create(request, *args, **kwargs)
        else:
            return Response("Access Denied")
            #return HttpResponse("Access denied")

#class BookList(APIView):
    #def get(self, request, format=None):
        #books = Book.objects.all()
        #serializer = BookSerializer(books, many=True)
        #return Response(serializer.data) 

    #def post(self, request, fromat=None):
        #serializer = BookSerializer(data= request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@api_view(['GET', 'POST'])
#def book_list(request):
    
    #if request.method == 'GET':
        #books = Book.objects.all()
        #serializer = BookSerializer(books, many=True)
        #return Response(serializer.data)
    #elif request.method == 'POST':
        #serializer = BookSerializer(data= request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
