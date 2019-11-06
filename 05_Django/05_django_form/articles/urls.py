from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),  # CREATE Logic 2 - 데이터베이스에 저장
    path('<int:article_pk>/', views.detail, name='detail'),    # READ Logic - Detail
    path('<int:article_pk>/delete/', views.delete, name='delete'),    # READ Logic - Detail
    path('<int:article_pk>/update/', views.update, name='update'),    # READ Logic - Detail
]