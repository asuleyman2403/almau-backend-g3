from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView,\
    RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateAPIView, \
    RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import Response
from blogs.serializers import PostSerializer
from blogs.models import Blog, Post


class ListCreatePostAPIView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class BlogsPostsAPIView(ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        try:
            blog = Blog.objects.get(id=self.kwargs['pk'])
            posts = blog.posts.all()
            return posts
        except:
            pass

    def post(self, request, *args, **kwargs):
        data = request.data
        data['blog_id'] = kwargs['pk']
        serializer = PostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)








class ListPostAPIView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CreatePostAPIView(CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class RetrievePostAPIView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class UpdatePostAPIView(UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class DeletePostAPIView(DestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class RetrieveUpdatePostAPIView(RetrieveUpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class RetrieveDestroyPostAPIView(RetrieveDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()



