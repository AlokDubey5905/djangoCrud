from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('api/blogs/', views.all_blogs_api, name='all_blogs_api'),
    path('api/blog/<int:blog_id>/', views.getBlogById, name='blog_by_id_api'),
    path('api/user_blogs/',login_required(views.user_blogs_api), name='user_blogs_api'),
    path('api/signup/', views.signup_api, name='signup_api'),
    path('api/login/', views.login_api, name='login_api'),
    path('api/logout/', login_required(views.logout_api), name='logout_api'),
    path('api/current_user/', views.current_user_api, name='current_user_api'),
    path('api/add_blog/', login_required(views.add_blog_api), name='add_blog_api'),
    path('api/edit_blog/<int:blog_id>/', login_required(views.edit_blog_api), name='edit_blog_api'),
    path('api/delete_blog/<int:blog_id>/', login_required(views.delete_blog_api), name='delete_blog_api'),
    path('api/search/', views.search_blogs, name='search_blogs_api'),
    path('', views.blog_list, name='blog_list'),
    path('userblogs/', views.user_blog_list, name='user_blog_list'),
    path('add/', login_required(views.add_blog), name='add_blog'),
    path('edit/<int:pk>/', login_required(views.edit_blog), name='edit_blog'),
    path('delete/<int:pk>/', login_required(views.delete_blog), name='delete_blog'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]
