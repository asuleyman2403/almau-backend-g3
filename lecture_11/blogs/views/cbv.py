from rest_framework.views import APIView
from rest_framework.response import Response
from blogs.models import Blog
from blogs.serializers import BlogSerializer, PostSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class ListCreateBlogAPIView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        data['owner_id'] = request.user.id
        serializer = BlogSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


# class RetrieveUpdateDestroyBlogAPIView(APIView):
class BlogAPIView(APIView):
    def get_blog(self, pk):
        try:
            blog = Blog.objects.get(id=pk)
            return blog
        except Blog.DoesNotExist:
            return None

    def get(self, request, pk):
        blog = self.get_blog(pk)
        if blog is not None:
            serializer = BlogSerializer(blog)
            return Response(serializer.data, status=200)
        else:
            return Response({'message': 'Not found'}, status=404)

    def put(self, request, pk):
        blog = self.get_blog(pk)
        if blog is not None:
            data = request.data
            data['owner_id'] = request.user.id
            serializer = BlogSerializer(data=data, instance=blog)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response({'message': 'Not found'}, status=404)

    def delete(self, request, pk):
        blog = self.get_blog(pk)
        if blog is not None:
            blog.delete()
            return Response({'message': 'Success!'}, status=200)
        else:
            return Response({'message': 'Not found'}, status=404)