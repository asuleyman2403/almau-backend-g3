from django.urls import path, include
from blogs.views.fbv import list_create_blogs
from blogs.views.cbv import ListCreateBlogAPIView, BlogAPIView
from blogs.views.generics import ListPostAPIView, CreatePostAPIView, ListCreatePostAPIView, \
    RetrievePostAPIView, UpdatePostAPIView, DeletePostAPIView, PostAPIView, BlogsPostsAPIView


urlpatterns = [
    # path('', list_create_blogs),
    path('blogs/', ListCreateBlogAPIView.as_view()),
    path('blogs/<int:pk>', BlogAPIView.as_view()),
    path('blogs/<int:pk>/posts', BlogsPostsAPIView.as_view()),
    path('posts/', ListCreatePostAPIView.as_view()),
    path('posts/<int:pk>/', PostAPIView.as_view()),
    # path('admin/', admin.site.urls),
]
