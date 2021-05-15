from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.homepage, name='home'),
    path('login', views.login_request, name='login'),
    path("register", views.register_request, name="register")
]