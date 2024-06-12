from django.urls import path
from .import views
urlpatterns = [
    path('', views.index),
    path('create/', views.create_geeksmodel, name='create_geeksmodel'),
    path('read/', views.read_geeksmodel , name='read_geeksmodel'),
    path('edit/', views.edit_geekmodel , name='edit_geeksmodel'),
    path('delete/', views.delete_geekmodel , name='delete_geeksmodel'),
]
