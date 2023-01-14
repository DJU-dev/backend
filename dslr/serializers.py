from django.contrib.auth import get_user_model
from rest_framework import serializers
from dslr.models import Post

class AutherSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']


class PostSerializers(serializers.ModelSerializer):
    author = AutherSerializers(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'