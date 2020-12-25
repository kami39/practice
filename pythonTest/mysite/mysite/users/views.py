# -*- coding: utf-8 -*-

# from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.contrib.auth import *

from django import forms

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

def first_page(request):
    return HttpResponse("<p>用户</p>")

def register(request): 
    if request.method == 'POST': 
        form = UserCreationForm(request.POST) 
        if form.is_valid(): 
            new_user = form.save() 
        return redirect("/") 
    else:
        form = UserCreationForm()
        ctx = {'form': form}
        ctx.update(csrf(request))       
        return render(request, "register.html", ctx)



# def user_login(request):
#     if request.POST:
#         username = password = ''
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user     = authenticate(username=username, password=password)
#         if user is not None and user.is_active:
#             login(request, user)
#             # return redirect('/')
#             # return redirect('/users/diff_response')
#             # return redirect('/users/user_only')
#             return redirect('/users/specific_user')
#             # return HttpResponse("here now")
#         else:
#             return redirect('/users/diff_response')


#     ctx = {}
#     ctx.update(csrf(request))
#     return render(request, 'login.html',ctx)



# #user with form
# def user_login(request):
#     ctx = {}
#     if request.POST:
#         return render(request, 'login_v2.html',ctx)  
        
#     return render(request, 'login.html',ctx)

def user_login(request):
    return HttpResponse("<p>你好</p>")

def user_logout(request):
    '''
    logout
    URL: /users/logout
    '''
    logout(request)
    return redirect('/')

def diff_response(request):
    if request.user.is_authenticated():
        # content = "<p>my dear user</p>"
        content = request.user.get_username()
        # request.user.set_password('django')
    else:
        content = "<p>you wired stranger</p>"
    return HttpResponse(content)

@login_required
def user_only(request):
    return HttpResponse("<p>This message is for logged in user only.</p>")


# decorators of user_passes_test
def name_check(user):
    return user.get_username() == 'django'

@user_passes_test(name_check)
def specific_user(request):
    return HttpResponse("<p>for django only</p>")


        
