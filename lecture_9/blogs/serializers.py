from rest_framework import serializers
from blogs.models import Blog, Post


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ['id', 'title']
        # fields = ('id', 'title',)


class PostSerializer(serializers.ModelSerializer):
    content = serializers.CharField(min_length=10, max_length=500)

    class Meta:
        model = Post
        fields = '__all__'
