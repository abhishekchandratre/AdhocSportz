from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Events, UserInfo, Location, Sports, SportsType, UserFriends



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'country', 'state', 'region')


class SportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsType
        fields = ('categoryName',)


class SportsSerializer(serializers.ModelSerializer):
    sportType = SportTypeSerializer()

    class Meta:
        model = Sports
        fields = ('sportName', 'sportType','sportImage')


class UserInfoSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    location = LocationSerializer()
    sports = SportsSerializer(read_only=True, many=True)

    class Meta:
        model = UserInfo
        fields = ('user', 'gender', 'location', 'phoneNumber', 'oneLinerStatus', 'sports')


class EventSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    location = LocationSerializer()
    sport = SportsSerializer()
    class Meta:
        model = Events
        fields = ('id', 'owner', 'sport', 'name', 'desc', 'numberOfPlayers', 'startDate', 'eventType', 'location')


class EventInfoSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    location = LocationSerializer()

    class Meta:
        model = Events
        fields = ('id', 'owner', 'sport', 'name', 'desc', 'numberOfPlayers', 'startDate', 'location')


class UserFriendsSerializer(serializers.ModelSerializer):
    friends = UserInfoSerializer(read_only=True,many=True)

    class Meta:
        model = UserFriends
        fields = ('friends',)
