from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_request, name='login'),
    path('register', views.register_request, name='register'),
    path('logout', views.logout_request, name='logout'),  # To be removed
    path('changepassword', views.change_password, name='changepassword'),
    path('dashboard', views.dashboard_request, name='dashboard'),
    path('clients', views.clients_request, name='clients'),
    path('dread', views.dread_request, name='dread'),
    path("password_reset", views.password_reset_request, name="password_reset"), 
    path("reset_done",views.password_reset_done, name="password_reset_done"),
]
