from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from .forms import *
from .models import *
# Create your views here.
def home(request):
    return render(request, 'home.html', locals())

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    # 登入
    elif 'login' in request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form["user_id"].value()
            password = form["password"].value()
            user = auth.authenticate(username = username, password = password)
            if user != None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/')
            else:
                login_failed = True
    #reload page
    form = LoginForm()
    return render(request, 'login.html', locals())

@login_required
def logout(request):
    auth.logout(request)
    return render(request, 'logout.html', locals())

def register(request):
    if request.method == 'POST':
        new_user = UserCreationForm(request.POST)
        user_data = RegisterForm(request.POST)
        if new_user.is_valid() and user_data.is_valid():
            # 註冊帳戶
            new_user = new_user.save()
            # 儲存個資
            name = user_data['name'].value()
            gender = user_data['gender'].value()
            UserData.objects.create(name = name, gender = gender, user_id = new_user)
            return HttpResponseRedirect('/home/')
    else:
        new_user = UserCreationForm()
        user_data = RegisterForm()
    return render(request, 'register.html', locals())