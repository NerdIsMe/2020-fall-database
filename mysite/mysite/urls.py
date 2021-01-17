"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from zoo_info.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('accounts/login/', login),
    path('accounts/logout/', logout),
    path('accounts/register/', register),
    path('search/zoo/', zoo_list),

    # Search 
    path('search/', search_menu),
    path('search/animal/', search_animal),
    path('search/animal/<int:animal_id>/', animal_info),
    path('search/individual_animal/<int:individual_id>', individual_animal),
    path('search/zookeeper/', search_zookeeper),
    path('search/zookeeper/<int:keeper_id>/', zookeeper_feed_info),
    path('search/area/', search_area),
    path('search/area/<int:area_id>/', area_info),
    path('search/habitat/', search_habitat),

    # superuser
    path('search/zookeeper/insert/', superuser_zookeeper_insert),
    path('search/zookeeper/<int:keeper_id>/modify_personal_info/', superuser_zookeeper_modify_personal_info),
    path('search/zookeeper/<int:keeper_id>/modify_animal/', superuser_zookeeper_modify_animal),
]
