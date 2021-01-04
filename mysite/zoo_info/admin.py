from django.contrib import admin
# Register your models here.
from .models import UserData, Zoo, Area, Habitat, Zookeeper

class UserDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'user_id')
    list_filter = ('name', 'gender')

class ZooAdmin(admin.ModelAdmin):
    list_display = ('zoo_id', 'number_of_visitors', 'number_of_categories', 'ticket_price')
    list_filter = ('number_of_visitors', 'number_of_categories')

# class AreaAdmin(admin.ModelAdmin):
#     list_display('Area_id', 'position', 'nearby')

class ZookeeperAdmin(admin.ModelAdmin):
    list_display = ('keeper_id', 'name', 'join_time', 'department', 'birth')
    #list_filter = ('number_of_visitors', 'number_of_categories')

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('scientific_id', 'animal_name', 'category')#, 'conservation')

admin.site.register(UserData, UserDataAdmin)
admin.site.register(Zoo, ZooAdmin)
admin.site.register(Zookeeper, ZookeeperAdmin)
#admin.site.register(Animal, AnimalAdmin)