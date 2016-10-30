from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Events, UserInfo



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id', 'owner', 'sport', 'name', 'desc', 'numberOfPlayers', 'startDate', 'location')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class UserInfoSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserInfo
        fields = ('user','gender')

