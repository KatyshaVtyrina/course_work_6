from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostListView, PostDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('blog', PostListView.as_view(), name='post_list'),
    path('blog', PostDetailView.as_view(), name='post_detail'),
]