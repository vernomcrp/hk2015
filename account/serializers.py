from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account, GroupAccount


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('user', 'group', 'is_admin')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password')

class GroupAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupAccount
