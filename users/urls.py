from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login),
    path('details/', views.user_details),
    path('resume/', views.user_resume)
]
