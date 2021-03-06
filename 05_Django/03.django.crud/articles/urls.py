from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:article_pk>/update/', views.update, name='update'),
    # path('<int:article_pk>/edit/', views.edit, name='edit'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),  # delete logic

    path('<int:article_pk>/', views.detail, name='detail'),
    path('create/', views.create),  # GET(new) / POST(create)
    # path('new/', views.new),
    path('', views.index, name='index'),
]
