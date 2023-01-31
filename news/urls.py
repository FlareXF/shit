from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewsListView.as_view(), name='news'),
    path('post/<int:pk>/', views.NewsDetailView.as_view(), name='post-detail'),
    path('post/new/', views.CreatePostView.as_view(), name='create-post')
]
