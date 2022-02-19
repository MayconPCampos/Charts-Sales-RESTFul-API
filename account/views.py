from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from django.contrib.auth.models import User


class Users(APIView):

    def get(self, request):
        """Retorna as informações dos usuários cadastrados"""
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data) # retorna os nome de usuários
        

    def post(self, request):
        """Cria um novo registro de usuário"""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
