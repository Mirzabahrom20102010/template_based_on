from django.urls import path

from .views import PostView, PostDetailView, CreatePostView

app_name = 'posts'

urlpatterns = [
    path('', PostView.as_view(), name='post-list'),
    path('detail/<int:id>', PostDetailView.as_view(), name='post-detail'),
    path('create/', CreatePostView.as_view(), name='create-post'),
]
