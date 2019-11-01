from django.contrib import admin
from django.urls import path
from . import views

app_name = 'movieapp'
urlpatterns = [
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/edit/', views.edit, name='edit'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('create/', views.create),
    path('new/', views.new),
    path('', views.index, name='index')
]
