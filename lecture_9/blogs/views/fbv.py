from rest_framework.decorators import api_view
from rest_framework.response import Response
from blogs.models import Blog
from blogs.serializers import BlogSerializer, PostSerializer


@api_view(['GET', 'POST'])
def list_create_blogs(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=200)

    if request.method == 'POST':
        data = request.data
        serializer = BlogSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


# @api_view(['GET', 'PUT', 'DELETE'])
# def list_create_blogs(request, pk):
#     if request.method == 'GET':
#         blogs = Blog.objects.all()
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data, status=200)
#
#     if request.method == 'POST':
#         data = request.data
#         serializer = BlogSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)
