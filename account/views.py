from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from .models import Account, GroupAccount
from rest_framework import viewsets
from .serializers import AccountSerializer, UserSerializer, GroupAccountSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class GroupAccountViewSet(viewsets.ModelViewSet):
    queryset = GroupAccount.objects.all()
    serializer_class = GroupAccountSerializer
