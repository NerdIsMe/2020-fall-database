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

def zoo_list(request):
    zoo_data = Zoo.objects.all()
    return render(request, 'zoo_info/zoo_list.html', locals())


# search
def search_menu(request):
    return render(request, 'zoo_info/search_menu.html', locals())

def search_animal(request):
    if 'animal_name' in request.GET:
        animal_name = request.GET['animal_name']
        animal_info = Animal.objects.filter(animal_name__contains = animal_name)
    else:
        animal_info = Animal.objects.all()
    return render(request, 'zoo_info/search_by/animal.html', locals())

def animal_info(request, animal_id):
    animal = Animal.objects.get(animal_id = animal_id)
    feed = Feed.objects.get(animal_id = animal_id)
    return render(request, 'zoo_info/search_by/animal_info.html', locals())

def individual_animal(request, individual_id):
    individual_animal = IndividualAnimal.objects.get(id = individual_id)
    return render(request, 'zoo_info/search_by/individual_animal.html', locals())

def search_zookeeper(request):
    current_year = 2021
    if 'zookeeper_name' in request.GET:
        zookeeper_name = request.GET['zookeeper_name']
        zookeeper_info = Zookeeper.objects.filter(name__contains = zookeeper_name)
    else:
        zookeeper_info = Zookeeper.objects.all()
    return render(request, 'zoo_info/search_by/zookeeper.html', locals())

def zookeeper_feed_info(request, keeper_id): 
    current_year = 2021
    zookeeper = Zookeeper.objects.get(keeper_id = keeper_id)
    feeds = Feed.objects.filter(keeper_id = zookeeper)
    return render(request, 'zoo_info/search_by/zookeeper_feed_info.html', locals())

def search_area(request):
    if 'area_name' in request.GET:
        area_name = request.GET['area_name']
        area_info = Area.objects.filter(theme__contains = area_name)
    else:
        area_info = Area.objects.all()
    return render(request, 'zoo_info/search_by/area.html', locals())

def area_info(request, area_id):
    area = Area.objects.get(area_id = area_id)
    animal_info = Animal.objects.filter(area_id = area)
    facilities = Facility.objects.filter(area_id = area)
    return render(request, 'zoo_info/search_by/area_info.html', locals())

def search_habitat(request):
    if 'habitat_name' in request.GET:
        habitat_name = request.GET['habitat_name']

        # weather
        habitat_info = Habitat.objects.filter(weather__contains = habitat_name)
        # continent
        if habitat_info.count() == 0:
            habitat_info = Habitat.objects.filter(continent__contains = habitat_name)
        # terrain
        if habitat_info.count() == 0:
            habitat_info = Habitat.objects.filter(terrian__contains = habitat_name)
    else:
        habitat_info = Habitat.objects.all()
    return render(request, 'zoo_info/search_by/habitat.html', locals())

# super user
@login_required
def superuser_zookeeper_insert(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/home/')
    
    if 'z_id' in request.POST:
        new_zookeeper = Zookeeper()
        new_zookeeper.keeper_id = int(request.POST['z_id'])
        new_zookeeper.name = request.POST['z_name']
        new_zookeeper.join_time = int(request.POST['z_join_time'])
        new_zookeeper.birth = int(request.POST['z_birth'])
        new_zookeeper.area_id = Area.objects.get(area_id = request.POST['z_area_id'])
        new_zookeeper.save()
        return HttpResponseRedirect('../')

    return render(request, 'zoo_info/superuser/zookeeper_insert.html', locals())


@login_required
def superuser_zookeeper_modify_personal_info(request, keeper_id):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/home/')
    the_zookeeper = Zookeeper.objects.get(keeper_id = keeper_id)
    if 'z_name' in request.POST:
        the_zookeeper.name = request.POST['z_name']
        the_zookeeper.join_time = int(request.POST['z_join_time'])
        the_zookeeper.birth = int(request.POST['z_birth'])
        the_zookeeper.area_id = Area.objects.get(area_id = request.POST['z_area_id'])
        the_zookeeper.save()
        return HttpResponseRedirect('../')

    return render(request, 'zoo_info/superuser/zookeeper_modify_personal_info.html', locals())