from django.urls import path
from . import views

urlpatterns = [
    path('static_sample/', views.static_sample),
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('result/', views.result),
    path('art/', views.art),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('index/', views.index)
    # /localhost/pages/
]