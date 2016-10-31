from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import RegistrationForm, LoginForm, SportsInterestForm, UserInfoForm, EventForm, LocationForm
from .models import SportsType, Sports, UserInfo, Events, Location
from .serializer import EventSerializer, UserSerializer, UserInfoSerializer, SportsSerializer, EventInfoSerializer


# Create your views here.
@login_required
def index(request):
    token = {}
    token['fullname'] = request.user
    return render_to_response("core/index.html", token)


def test(request):
    pass


# @login_required
def registerBasic(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return HttpResponseRedirect('core/register/userInfo')

    else:
        form = RegistrationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form
    return render_to_response('core/register/basic.html', token)


@login_required
def registerUserInfo(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            userInfoObj = form.save(commit=False)
            userInfoObj.user = request.user
            userInfoObj.save()
            return HttpResponseRedirect('/core/register/sportsInterest')

    else:
        form = UserInfoForm()
    token = dict()
    token.update(csrf(request))
    token['form'] = form
    return render_to_response('core/register/userInfo.html', token)


@login_required
def registersSportsInterest(request):
    if request.method == 'POST':
        choices = getSportChoices()
        form = SportsInterestForm(request.POST, choices=choices)
        if form.is_valid():
            userInfoObj = UserInfo.objects.get(user=request.user)
            print(userInfoObj.birthDate)
            form.save(choices, userInfoObj)
            return HttpResponseRedirect('/core/')

    else:
        choices = getSportChoices()
        form = SportsInterestForm(choices=choices)
    token = dict()
    token.update(csrf(request))
    token['form'] = form
    return render_to_response('core/register/sportsInterest.html', token)


def getSportChoices():
    sports_dict = {}
    sport_types = SportsType.objects.values()
    for sport_type in sport_types:
        sport_list = Sports.objects.values().filter(sportType=sport_type['id'])
        sports = []
        for sport in sport_list:
            sports.append(sport['sportName'])
        sports_dict[sport_type['categoryName']] = sports

    return sports_dict


def registration_complete(request):
    return render_to_response('core/register/registration_complete.html')


def logout_user(request):
    logout(request)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('core/register/complete')

    form = LoginForm()
    context = {}
    context.update(csrf(request))
    context['form'] = form
    return render_to_response('core/register/login.html', context)


@api_view(['GET'])
def eventCollection(request):
    if request.method == 'GET':
        try:
            events = Events.objects.all()
        except Events.DoesNotExist:
            return HttpResponse(status=404)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def eventDetails(request, pk):
    try:
        event = Events.objects.get(id=pk)
    except Events.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = EventInfoSerializer(event)
        return Response(serializer.data)


@login_required
def eventCreate(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user
            location = Location.objects.get_or_create(country='India', state='MH', region='Pune')
            location = Location.objects.get(country='India', state='MH', region='Pune')
            event.location = location
            event.save()
            return HttpResponseRedirect('/core/')

    else:
        form = EventForm()
    context = dict()
    context.update(csrf(request))
    context['form'] = form
    return render_to_response('core/register/eventCreate.html', context)


@api_view(['GET'])
def userCollection(request):
    if request.method == 'GET':
        users = User.objects.all()
        serialize = UserSerializer(users, many=True)
        return Response(serialize.data)


@api_view(['GET'])
def userDetails(request, pk):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=pk)
            userObj = UserInfo.objects.get(user=user)
        except UserInfo.DoesNotExist:
            return HttpResponse(status=404)
        serialize = UserInfoSerializer(userObj)
        return Response(serialize.data)


@api_view(['GET'])
def sportCollection(request):
    if request.method == 'GET':
        sports = Sports.objects.all()
        serialize = SportsSerializer(sports, many=True)
        return Response(serialize.data)
