from django.db import models


class Blog(models.Model):
    title = models.CharField(null=False, max_length=255)
    description = models.TextField(null=False, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


class Post(models.Model):
    title = models.CharField(null=False, max_length=255)
    content = models.CharField(null=False, max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

