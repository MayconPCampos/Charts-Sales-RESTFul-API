from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sale
from .serializer import SaleSerializer
from django.http import Http404
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class SaleList(APIView):

    # Aplicando restrição onde apenas usuários
    # autenticados podem ver e alterar seus dados
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly
    ]

    def get(self, request):
        """Retorna todas as entradas de vendas"""
        sales = Sale.objects.all()
        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data)


    def post(self, request):
        """Adiciona uma nova entrada"""
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user) # relaciona o usuário à entrada
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SaleDetail(APIView):

    # Aplicando restrição onde apenas usuários
    # autenticados podem alterar seus dados
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        """Busca o recurso pelo id, retorna
        um erro http 404 caso não seja encontrado"""
        try:
            return Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        """Retorna a entrada de venda de acordo com a pk"""
        sale = self.get_object(pk)
        serializer = SaleSerializer(sale)
        return Response(serializer.data)


    def put(self, request, pk):
        """Atualiza uma entrada de venda"""
        sale = self.get_object(pk)
        serializer = SaleSerializer(sale, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user) # relaciona o usuário à entrada
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        """Atualiza um ou mais dados de uma entrada"""
        sale = self.get_object(pk)
        serializer = SaleSerializer(sale, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        """Remove uma entrada de venda"""
        sale = self.get_object(pk)
        sale.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
