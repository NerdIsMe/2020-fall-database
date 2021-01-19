from django.contrib import admin
# Register your models here.
from .models import UserData, Zoo, Area, Habitat, Zookeeper, Animal, IndividualAnimal

class UserDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'user_id')
    list_filter = ('name', 'gender')

class ZooAdmin(admin.ModelAdmin):
    list_display = ('zoo_id', 'number_of_visitors', 'number_of_categories', 'ticket_price')
    list_filter = ('number_of_visitors', 'number_of_categories')

# class AreaAdmin(admin.ModelAdmin):
#     list_display('Area_id', 'position', 'nearby')

class ZookeeperAdmin(admin.ModelAdmin):
    list_display = ('keeper_id', 'name', 'join_time', 'area_id', 'birth')
    #list_filter = ('number_of_visitors', 'number_of_categories')

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('animal_name', 'scientific_id', 'category')#, 'conservation')
    search_fields = (['animal_name'])

class IndividualAnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'animal_id')#, 'conservation')
    search_fields = (['name'])

admin.site.register(UserData, UserDataAdmin)
admin.site.register(Zoo, ZooAdmin)
admin.site.register(Zookeeper, ZookeeperAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(IndividualAnimal, IndividualAnimalAdmin)