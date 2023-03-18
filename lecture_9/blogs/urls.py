from django.urls import path, include
from blogs.views.fbv import list_create_blogs
from blogs.views.cbv import ListCreateBlogAPIView, BlogAPIView


urlpatterns = [
    # path('', list_create_blogs),
    path('', ListCreateBlogAPIView.as_view()),
    path('<int:pk>', BlogAPIView.as_view())
    # path('admin/', admin.site.urls),
]
