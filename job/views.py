from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from.models import *
from.forms import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def admin_login(request):
    return render(request,'admin_login.html')

def user_login(request):
    if request.user.is_authenticated:

        return redirect('/')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')



        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'Email or Password Does Not Matched')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('user_home')

    return render(request,'user_login.html')


def Logout(request):
    logout(request)
    return redirect('index')

def recruiter_login(request):
    return render(request,'recruiter_login.html')

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request,'user_home.html')

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    usercreate = CreateUser()
    stucreate = StudentCreate()
    if request.method == 'POST':
        usercreate = CreateUser(request.POST, request.FILES)
        stucreate = StudentCreate(request.POST, request.FILES)
        if usercreate.is_valid() & stucreate.is_valid():
            user = usercreate.save()
            stucreate = stucreate.save(False)
            stucreate.user = user
            stucreate.save()
            messages.success(request, 'User account was created!')
            return redirect('user_login')

        else:
            messages.error(request, 'An error has occurred during registration')

    context = {'usercreate':usercreate, 'stucreate':stucreate}
    return render(request,'user_signup.html', context)

def select_user(request):
    return render(request, 'select_user.html')

def recruiter_signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    usercreate = CreateUser()
    reqcreate = RecuriterCreate()
    if request.method == 'POST':
        usercreate = CreateUser(request.POST, request.FILES)
        reqcreate = RecuriterCreate(request.POST, request.FILES)
        if usercreate.is_valid() & reqcreate.is_valid():
            user = usercreate.save()
            user.is_active = False
            reqcreate = reqcreate.save(False)
            reqcreate.user = user

            reqcreate.save()
        return redirect('user_login')
    context = {'usercreate':usercreate, 'reqcreate':reqcreate}
    return render(request, 'recruiter_signup.html', context)


def logoutuser(request):
    logout(request)
    return redirect('index')