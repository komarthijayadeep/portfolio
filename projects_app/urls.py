from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/add/', views.project_create, name='project_create'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('projects/<slug:slug>/delete/', views.project_delete, name='project_delete'),
]
