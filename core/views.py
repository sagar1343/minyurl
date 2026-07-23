from django.contrib.auth.models import User
from .serializers import UserCreateSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from rest_framework import status


# Create your views here.
class UserRegisterView(CreateAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get("username")
        exists = User.objects.filter(username=username).exists()
        if exists:
            return Response(
                {"message": "already registered"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return Response(serializer.data)
