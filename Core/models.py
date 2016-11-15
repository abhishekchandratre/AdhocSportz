from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Location(models.Model):
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    region = models.CharField(max_length=200)

    class Meta:
        unique_together = ('country', 'state', 'region')

    def __str__(self):
        return self.country + ', ' + self.state + ', ' + self.region


class Sports(models.Model):
    sportName = models.CharField(max_length=140)
    sportType = models.ForeignKey('SportsType')
    sportImage = models.FileField(upload_to='sport_img/',null=True)

    def __str__(self):
        return self.sportName


class UserInfo(models.Model):
    user = models.OneToOneField(User)
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Not Mentioned'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    birthDate = models.DateField(auto_now=False, auto_now_add=False)
    phoneRegex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phoneNumber = models.CharField(validators=[phoneRegex], blank=True,max_length=16)
    oneLinerStatus = models.CharField(max_length=140)
    location = models.ForeignKey(Location, null=True)
    #profilePicture = models.ImageField(null=True)
    sports = models.ManyToManyField(Sports)

    def __str__(self):
        return self.user.first_name + self.user.last_name + str(self.sports.values())


class SportsType(models.Model):
    categoryName = models.CharField(max_length=140)

    def __str__(self):
        return self.categoryName


class Events(models.Model):
    owner = models.ForeignKey(User)
    sport = models.ForeignKey(Sports)
    name = models.CharField(max_length=80)
    desc = models.CharField(max_length=250)
    startDate = models.DateField()
    location = models.ForeignKey(Location)
    numberOfPlayers = models.IntegerField(default=1)
    EVENT_CHOICE = (
        ('Public', 'Public'),
        ('Private', 'Private'),
    )
    eventType = models.CharField(max_length=10, choices=EVENT_CHOICE)
    #EventPicture = models.ImageField(null=True)


class UserFriends(models.Model):
    user = models.OneToOneField(User)
    friends = models.ManyToManyField(UserInfo)

class EventPlayers(models.Model):
    event = models.ForeignKey(Events)
    players = models.ForeignKey(UserInfo)

    class Meta:
        unique_together = ('event', 'players')
