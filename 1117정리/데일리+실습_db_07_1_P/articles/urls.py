from django.urls import path
from . import views


urlpatterns = [
    path('html/', views.article_html),
    path('json-1/', views.article_json_1),
    path('json-2/', views.article_json_2),
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comments_list),
    path('comments/<int:comment_pk>/', views.comments_detail),
    path('articles/<int:article_pk>/comments/', views.comments_create),
]
