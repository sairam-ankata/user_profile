from django.contrib import admin
from users.models import User, UserResume


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ("username", "email")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.filter(is_deleted=False)
        return qs


class UserResumeAdmin(admin.ModelAdmin):
    list_display = ("user_name", "url", "date_of_adding")

    def user_name(self, obj):
        return obj.user.username

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.filter(user__is_deleted=False)
        return qs


admin.site.register(User, UserAccountAdmin)
admin.site.register(UserResume, UserResumeAdmin)

