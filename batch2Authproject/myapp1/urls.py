from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
urlpatterns = [
    path('register/',views.register_user,name="register"),
    ]
