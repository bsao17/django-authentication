from django.contrib import admin

from .models import CustomUser, Profile


# Register your models here.
@admin.register(CustomUser)
class My_admin_User(admin.ModelAdmin):
    pass


@admin.register(Profile)
class My_Profile_Admin(admin.ModelAdmin):
    pass
