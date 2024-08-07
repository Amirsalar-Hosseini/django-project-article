from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('register/', views.register_page, name='register_page'),
]