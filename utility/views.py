from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import dynamic


# Create your views here.


def index(request):
    sun = dynamic.objects.all()
    return render(request, "templates/index.html", {'first': sun})


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first name']
        last_name = request.POST['last name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['confirm password']
        if len(first_name) == 0:
            messages.info(request, 'please enter your First name')
            return redirect('register')
        elif len(last_name) == 0:
            messages.info(request, 'please enter your Last name')
            return redirect('register')
        elif len(username) == 0:
            messages.info(request, 'please enter your Username')
            return redirect('register')
        elif len(email) == 0:
            messages.info(request, 'please enter your Email')
            return redirect('register')
        elif len(password) == 0:
            messages.info(request, 'please enter your Password')
            return redirect('register')
        elif password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Is Already Exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.success(request, 'Email Is Already Exist')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                                username=username, email=email, password=password)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request, 'password not match!!!')
            return redirect('register')

    else:
        return render(request, 'templates/register.html')


def processed(request):
    return HttpResponse('''
                                hello!!! welcome 
                                <div class="a">
                                 
                                </div>
                                 <style>
                                 .a{
                                 height:200px;
                                 width:200px;
                                 margin:25px;
                                 padding:10px;
                                 border:2px solid blue;
                                 }
                                 </style>
                                <h1>we are at processed function</h1>
                                                    ''')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.success(request, 'Invalid username or password !!!')
            return redirect('login')
    else:
        return render(request, 'templates/login.html')


def logout(request):
    auth.logout(request)
    return redirect('preblock')


@login_required(login_url='abc')
def gallery(request):
    return render(request, 'templates/gallery.html')


def abc(request):
    return render(request, 'templates/abc.html')


def aboutus(request):
    return render(request, 'templates/aboutus.html')
