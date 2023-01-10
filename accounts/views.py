from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework import serializers

User = get_user_model()

class SignupSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SignupView(CreateAPIView):
    model = User
    serializer_class = SignupSerialzer
    permission_classes = [
        AllowAny
    ]
