from django.contrib.auth import get_user_model, login, logout
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from core.serializers import RegistrationSerializer, LoginSerializer, ProfileSerializer, UpdatePasswordSerializer

USER_MODEL = get_user_model()


class RegistrationView(generics.CreateAPIView):
    model = USER_MODEL
    serializer_class = RegistrationSerializer


class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request=request, user=user)
        return Response(serializer.data)


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = USER_MODEL.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):  # переопределяем метод get_object
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdatePasswordView(generics.UpdateAPIView):
    serializer_class = UpdatePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
