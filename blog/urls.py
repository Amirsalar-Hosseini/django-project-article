from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.blog_page, name='blog_page'),
    path('<int:article_id>/', views.article_page, name='article_page'),
    path('create/', views.create_article, name='create_article'),
    path('update/<int:article_id>/', views.update_article, name='update_article'),
    path('delete/<int:article_id>/', views.delete_article, name='delete_article'),
    path('category/<int:category_id>/', views.get_article_by_category, name='category_article'),
    path('author/<int:author_id>/', views.get_article_by_author, name='author_article'),
]