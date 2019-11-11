from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('password/', views.change_password, name='password'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]