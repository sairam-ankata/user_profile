from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, UserResume


# class UserAccountAdmin(UserAdmin):

admin.site.register(User)
admin.site.register(UserResume)

