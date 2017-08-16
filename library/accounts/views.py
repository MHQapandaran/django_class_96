from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from lib_base_model.models import User 

from django.template import loader
from django.http import HttpResponse

# Create your views here.

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return HttpResponse("Logged in")
    else:
        #ERR
        return HttpResponse("Wrong username or password")
    
def logout_view(request):
    logout(request)
    
def login_from_view(request):
    template = loader.get_template('accounts/login_form.html')
    return HttpResponse(template.render({}, request))
