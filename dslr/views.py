from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from dslr.models import Post
from dslr.serializers import PostSerializers

class ReadOnlyPostViewSet(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
