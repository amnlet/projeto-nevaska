from django.urls import path
from . import views

urlpatterns = [
    # login route
    path("login/", views.loginView, name='login'),
    
    # logout route
    path("logout/", views.logoutView, name='logout'),
    
    # main path, create budget
    path("", views.mainView, name='main'),
    path("create/", views.c_budget, name='create-budget'),
    
    # Rotas de delete
    
    path("delete/<str:pk>", views.deleteBudget, name='delete-budget'),
]