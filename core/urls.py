from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_request, name='login'),
    path('register', views.register_request, name='register'),
    path('logout', views.logout_request, name='logout'), # To be removed
    path('changepassword', views.change_password, name='changepassword'),
]