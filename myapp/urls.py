from django.urls import path
from . import views


urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('discoverPage/', views.discoverPage, name='discoverPage'),
    path('accountPage/', views.accountPage, name='accountPage'),
    path('ViewAccountPage/<str:pk>/', views.ViewAccountPage, name='ViewAccountPage'),

    path('registerPage/', views.registerPage, name='registerPage'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('logoutPage/', views.logoutPage, name='logoutPage'),

    path('userRegisterPage/', views.userRegisterPage, name='userRegisterPage'),

    
]

