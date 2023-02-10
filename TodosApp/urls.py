from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addTask', views.addTask, name='addTask'),
    path('deleteTask/<str:pk>/', views.deleteTask, name='deleteTask'),
    path('editTask/<str:pk>/', views.editTask, name='editTask'),
    path('updateTask/<str:pk>/', views.updateTask, name='updateTask')
]