from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from reviews.models import User, Titles, Genres, Categories, Reviews, Comments
from .serializers import (
    SignupSerializer,
    AuthSerializer,
)


class SignupView(APIView):
    def post(self, request):
        """Регистрация нового пользователя"""
        username = request.data.get('username', None)
        email = request.data.get('email', None)
        user = User.objects.filter(username=username, email=email)

        if len(user) == 0:
            serializer = SignupSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        # Генерация кода и отправка email:
        user = User.objects.get(username=username, email=email)
        confirmation_code = default_token_generator.make_token(user)
        send_mail(
            'Код для получения токена:',
            (f'{"-" * 79}\n\nusername:\n{username}\n\n'
             f'Код подтверждения:\n{confirmation_code}\n'),
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )

        return Response(request.data, status=status.HTTP_200_OK)


class AuthView(APIView):
    def post(self, request):
        """Получение токена"""
        serializer = AuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UsersViewSet(ModelViewSet):
    pass
