from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "password"]


    def create(self, request):
        """Salva ium novo model de usuário com senha
        criptografada"""
        user = User.objects.create(username=request["username"])
        user.set_password(request["password"])
        user.save()
        return user