from django.contrib.auth import get_user_model
from rest_framework import serializers
from dslr.models import Post

class AutherSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']


class PostSerializer(serializers.ModelSerializer):
    author = AutherSerializer(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'