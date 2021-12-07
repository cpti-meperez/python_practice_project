from django.contrib import admin
from .models import Department, User
from django.contrib.auth.admin import UserAdmin

class UserAdmin(UserAdmin):
    list_display =('email','username','is_admin','is_staff')
    search_fields = ('email','username')


    filter_horizontal =()
    list_filter = ()
    fieldsets=()
 
 # register models to django admin
admin.site.register(User,UserAdmin)
admin.site.register(Department)