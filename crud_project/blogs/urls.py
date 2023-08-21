from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns=[
    path('',views.blog_list,name='blog_list'),
    path('userblogs/',views.user_blog_list,name='user_blog_list'),
    path('add/',login_required(views.add_blog),name='add_blog'),
    path('edit/<int:pk>/',login_required(views.edit_blog),name='edit_blog'),
    path('delete/<int:pk>/',login_required(views.delete_blog),name='delete_blog'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]