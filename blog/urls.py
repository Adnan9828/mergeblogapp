from django.urls import path, include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
   
    path('', views.post_list, name='post_list'),
    path('category/<str:slug>/', views.category, name='category'),
    path('tags/<str:slug>/', views.tag, name='tag'),
    path('postcomment/', views.postcomment, name='postcomment'),
    path('post/<str:slug>/', views.post_detail, name='post_detail'),
    path('post-new/', views.post_new, name='post-new'),
    path('post/<str:slug>/edit/', views.post_edit, name='post_edit'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    path('user_edit/<int:user_id>/',views. edit_profile,name='edit-profile'),
    path('login/', views.user_login, name='user-login'),
    path('signup/', views.user_signup, name='user-signup'),
    path('signout/', views.user_signout, name='user-signout'),
    # path('profile/', views.edit_profile, name='edit-profile'),
    path('upload-profile-photo/', views.upload_profile_photo, name='upload_profile_photo'),
    path('comment_reply/', views.create_reply, name='create_reply'),


] 
