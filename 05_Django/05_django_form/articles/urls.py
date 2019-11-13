from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),  # CREATE Logic 2 - 데이터베이스에 저장
    path('<int:article_pk>/', views.detail, name='detail'),    # READ Logic - Detail
    path('<int:article_pk>/delete/', views.delete, name='delete'),    # READ Logic - Detail
    path('<int:article_pk>/update/', views.update, name='update'),    # READ Logic - Detail
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:article_pk>/like/', views.like, name='like'),
    path('<int:article_pk>/follow/<int:user_pk>/', views.follow, name='follow'),
    path('list/', views.list, name='list'),
    path('explore/', views.explore, name='explore'),
]