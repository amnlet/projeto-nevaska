from django.urls import path
from . import views

urlpatterns = [
    # login route
    path("login/", views.loginView, name='login'),
    
    # logout route
    path("logout/", views.logoutView, name='logout'),
    
    # main path
    path("", views.mainView, name='main'),
    
    # Rotas de delete
    
    path("delete/<str:pk>", views.deleteBudget, name='delete-budget'),
]