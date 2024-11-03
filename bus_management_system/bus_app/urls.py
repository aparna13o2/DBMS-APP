from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employees/', views.employee_list, name='employee_list'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('depots/', views.depot_list, name='depot_list'),
    path('buses/', views.bus_list, name='bus_list'),
    path('routes/', views.route_list, name='route_list'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='bus_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='bus_app/logout.html'), name='logout'),
]
