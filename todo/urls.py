
from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register),
    path('', views.home, name="home"),
    path('update/<int:pk>/', views.update, name="update"),
    path('add/', views.add, name="add"),
    path('delete/<int:pk>/', views.delete, name="delete"),
]
