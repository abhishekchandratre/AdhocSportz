from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Events, UserInfo, Location



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id', 'owner', 'sport', 'name', 'desc', 'numberOfPlayers', 'startDate', 'location')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'country', 'state', 'region')


class UserInfoSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    location = LocationSerializer()

    class Meta:
        model = UserInfo
        fields = ('user','gender','location', 'phoneNumber','oneLinerStatus','sport')

