from django.contrib import admin
# Register your models here.
from .models import UserData

class UserDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'user_id')
    list_filter = ('name', 'gender')

admin.site.register(UserData, UserDataAdmin)