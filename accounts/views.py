from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from accounts.serializers import ProfileSerializer
from rest_framework.response import Response
from dslr.models import Post

User = get_user_model()
class ProfileView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = ProfileSerializer(user)
        post_count = Post.objects.filter(author_id=pk).count()
        new_serializer = {'post_count': post_count}
        new_serializer.update(serializer.data)
        return Response(new_serializer)


class MyProfileView(APIView):
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)
        serializer = ProfileSerializer(user)
        post_count = Post.objects.filter(author=request.user).count()
        new_serializer = {'post_count': post_count}
        new_serializer.update(serializer.data)
        return Response(new_serializer)


