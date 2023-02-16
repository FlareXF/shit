from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewsListView.as_view(), name='news'),
    path('post/<int:pk>/', views.NewsDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.UpdatePostView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(), name='post-delete'),
    path('posts/user/<str:username>', views.UserNewsListView.as_view(), name='posts-user'),
    path('post/new/', views.CreatePostView.as_view(), name='create-post'),
]
