from django.contrib import admin

from django_api.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list=('id','name','email','phone','address')
    admin.site.register(User)
