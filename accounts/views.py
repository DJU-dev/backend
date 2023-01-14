from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from accounts.serializers import ProfileSerializer
from rest_framework.response import Response

User = get_user_model()
class ProfileView(APIView):
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)
        serializer = ProfileSerializer(user)
        print(serializer.data)
        return Response(serializer.data)


