from django.contrib import admin
from django.urls import path
from . import views

app_name = "crud"
urlpatterns = [
    path('', views.top , name="top"),
    path('crud/', views.lists , name="list" ),
    path('crud/new', views.create , name="new"),
    path('crud/edit/<int:pk>', views.edit , name="edit"),
    path('crud/delete/<int:pk>', views.delete , name="delete"),
    path('crud/detail/<int:pk>', views.detail , name="detail"),
]