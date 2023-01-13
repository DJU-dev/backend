from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet
from dslr.models import Post
from dslr.serializers import PostSerializers

class ReadOnlyPostViewSet(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [AllowAny]
