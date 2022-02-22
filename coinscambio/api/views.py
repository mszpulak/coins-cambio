from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.serializers import UsersSerializer, CoinsSerializer, AddCoinsSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Coins
from rest_framework import status
from copy import deepcopy


class UsersViewSet(ModelViewSet):

    queryset = User.objects.all().select_related('coins')
    serializer_class = UsersSerializer

    @action(detail=True, methods=['put'])
    def add_coins(self, request, pk=None):
        user = self.get_object()
        data = deepcopy(request.data)
        print(data)
        data['user'] = user
        if user.coins:
            serializer = AddCoinsSerializer(user.coins, data=data)
        else:
            serializer = AddCoinsSerializer(data=data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
