from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='crud-index'),
    path('edit/<id>/', views.edit, name='crud-edit'),
    path('delete/<id>/', views.delete, name='crud-delete'),
    path('add/', views.add, name='crud-add'),
    path('create/', views.create, name='crud-create'),
    path('update/<id>/', views.update, name='crud-update'),
]
