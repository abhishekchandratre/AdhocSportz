from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
import subprocess

from .forms import RegistrationForm, LoginForm, SportsInterestForm, UserInfoForm, EventForm, LocationForm
from .models import SportsType, Sports, UserInfo, Events, Location, EventPlayers, UserFriends
from .serializer import EventSerializer, UserSerializer, UserInfoSerializer, SportsSerializer, EventInfoSerializer, \
    UserFriendsSerializer


# Create your views here.
@login_required
def index(request):
    token = {'fullname': request.user}
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
            return HttpResponseRedirect('/core/register/userInfo')

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
            location = Location.objects.get_or_create(
                country=request.POST['country'],
                state=request.POST['state'],
                region=request.POST['city']
            )
            location = Location.objects.get(
                country=request.POST['country'],
                state=request.POST['state'],
                region=request.POST['city']
            )
            userInfoObj.location = location
            userInfoObj.profilePicture = request.FILES['profilePicture']
            userInfoObj.profilePicture.name = userInfoObj.user.username
            userInfoObj.save()
            subprocess.call(["./scripts/resize_img.sh", userInfoObj.profilePicture.path, ])
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
            request.session['fullname'] = request.user.first_name + ' ' + request.user.last_name
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
    events_dict = {}

    return render_to_response('core/register/registration_complete.html')


def homePage(request):
    return HttpResponseRedirect('/core/')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/core/')


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
                    request.session['fullname'] = request.user.first_name + ' ' + request.user.last_name

                    context = {'request': request}
                    return render_to_response('core/index.html', context)

    if request.user.is_authenticated():
        request.session['fullname'] = request.user.first_name + ' ' + request.user.last_name
        context = {'request': request}
        return render_to_response('core/index.html', context)

    form = LoginForm()
    context = {}
    context.update(csrf(request))
    context['form'] = form
    return render_to_response('core/register/login.html', context)


@api_view(['GET'])
def myEventCollection(request):
    if request.method == 'GET':
        print(Events.objects.filter(owner=request.user))
        try:
            eventID = EventPlayers.objects.filter(players=request.user.id).values('event_id')
            criterion1 = Q(owner_id=request.user.id)
            criterion2 = Q(id=eventID)
            events = Events.objects.filter(criterion1 | criterion2).order_by('startDate').reverse()
        except Events.DoesNotExist:
            return HttpResponse(status=404)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def eventCollection(request):
    if request.method == 'GET':
        try:
            criterion1 = ~Q(owner_id=request.user.id)
            criterion2 = ~Q(eventType='Private')
            events = Events.objects.filter(criterion1 & criterion2).order_by('startDate').reverse()
        except Events.DoesNotExist:
            return HttpResponse(status=404)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


@login_required
def eventApprove(request):
    if request.method == 'GET':
        userEvents = []
        userPlayers = []
        events = Events.objects.filter(owner=request.user.id).values()
        for event in events:
            userEvents.append(event['id'])
        allUsers = EventPlayers.objects.filter(event_id__in=userEvents).values()
        for user in allUsers:
            userPlayers.append(user['players_id'])
        users = User.objects.filter(id__in=userPlayers).values()
        return render_to_response("core/register/eventApprove.html",
                                  {'users': users, 'events': events, 'eventPlayers': allUsers})


@api_view(['GET'])
def privateEventCollection(request):
    if request.method == 'GET':
        try:
            userFriends = UserFriends.objects.filter(user=request.user)
            allEvents = []
            for row in userFriends:
                user = User.objects.get(id=row.friend.id)
                events = Events.objects.filter(owner=user, eventType='Private').values()
                for event in events:
                    allEvents.append(event['id'])
        except Events.DoesNotExist:
            return Response(None)
        allEventsObj = Events.objects.filter(id__in=allEvents)
        serializer = EventSerializer(allEventsObj, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def publicEventCollection(request):
    if request.method == 'GET':
        try:
            criterion1 = ~Q(owner_id=request.user.id)
            criterion2 = ~Q(eventType='Private')
            events = Events.objects.filter(criterion1 & criterion2).order_by('startDate').reverse()
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
            location = Location.objects.get_or_create(
                country=request.POST['country'],
                state=request.POST['state'],
                region=request.POST['city']
            )
            location = Location.objects.get(
                country=request.POST['country'],
                state=request.POST['state'],
                region=request.POST['city']
            )
            event.location = location
            event.save()
            return HttpResponseRedirect('/core/')

    else:
        form = EventForm()
    context = dict()
    context.update(csrf(request))
    context['form'] = form
    return render_to_response('core/register/eventCreate.html', context)


@login_required
def eventView(request):
    if request.method == 'GET':
        token = {}
        token = dict()
        token['id'] = request.user.id
        print(request.user.id)
        return render_to_response("core/register/eventView.html", token)


@login_required
def eventPlayerView(request, pk):
    if request.method == 'GET':
        players = []
        context = dict()
        event = Events.objects.get(id=pk)
        eventPlayers = EventPlayers.objects.filter(event_id=pk).values()
        for eventPlayer in eventPlayers:
            players.append(eventPlayer['players_id'])
        users = User.objects.filter(id__in=players).values()
        context['users'] = users
        context['event'] = event
        context.update(csrf(request))
        return render_to_response("core/register/eventPlayerView.html", context)


@login_required
@csrf_exempt
def eventJoin(request):
    if request.is_ajax():
        userInfoObj = UserInfo.objects.get(user=request.user)
        eventplayers = EventPlayers.objects.create(
            event_id=request.POST['eventID'],
            eventName=request.POST['eventName'],
            players=userInfoObj
        )
        eventplayers.save()
        playerID = request.user.id
        event = Events.objects.get(id=request.POST['eventID'])
        user = User.objects.get(id=playerID)
        subject = 'Thanks for joining the event: ' + event.name + ' ' + user.get_full_name()
        message = 'Welcome to the event ' + event.name + ' happening at ' + event.location.state + '!! We will get back to you soon once the event owner approves your request. \n Till then keep looking out for other events. \n Thanks, \n AdhocSports Team'
        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        # send_mail(subject,message,from_email,to_list,fail_silently=true)
        return HttpResponseRedirect('/core/')


@login_required
@csrf_exempt
def eventApproval(request):
    if request.is_ajax():
        eventplayers = EventPlayers.objects.get(
            id=request.POST['eventPlayerID'])
        eventplayers.approvalStatus = request.POST['approval']
        eventplayers.save()
        event = Events.objects.get(id=eventplayers.event_id)
        user = User.objects.get(id=eventplayers.players_id)
        if request.POST['approval'] == 'approve':
            subject = 'Congrats!! You have been approved for the event: ' + event.name + ' '
            message = 'Welcome ' + user.get_full_name() + 'to the event ' + event.name + ' happening at ' + event.location.state + '!! It\'s going to be a fun-filled event. \n Come on champ, Let\'s make this event a great success!!! . \n Thanks, \n AdhocSports Team'
        else:
            subject = 'Event owner has turned down your request for the event: ' + event.name + ' '
            message = 'Thanks for your Interest ' + user.get_full_name() + '!! We hate to say NO to your request but the slots have been filled already \n I would recommend you to try other events happening at your location. Let\'s meet up soon!!! . \n Thanks, \n AdhocSports Team'
        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        # send_mail(subject,message,from_email,to_list,fail_silently=true)
        return HttpResponseRedirect('/core/')


@login_required
def friendsprofileView(request, pk):
    if request.method == 'GET':
        token = {}
        token = dict()
        token['userId'] = request.user.id
        token['friendId'] = pk
        friends = UserFriends.objects.filter(id=pk)
        if friends.count() > 0:
            token['isFriend'] = "true"
        return render_to_response("core/friendsProfile.html", token)


@login_required
@csrf_exempt
def connect(request):
    if request.is_ajax():
        friend = User.objects.get(id=request.POST['friends'])
        userInfoObj = UserInfo.objects.get(user=request.user)
        userFriendObj = UserFriends.objects.create(
            user=friend, friend=userInfoObj, approvalStatus='U')
        userFriendObj.save()
        return HttpResponseRedirect('/core/')


@login_required
@csrf_exempt
def rating(request):
    if request.is_ajax():
        print(request.POST['rating'])
        print(request.POST['user'])
        return HttpResponseRedirect('/core/')


@login_required
@csrf_exempt
def acceptUser(request):
    if request.is_ajax():
        friend = User.objects.get(id=request.POST['id'])
        friendObj = UserInfo.objects.get(user=friend)
        user = request.user
        userObj = UserInfo.objects.get(user=user)
        userFriend1 = UserFriends.objects.get(user=user, friend=friendObj)
        userFriend1.approvalStatus = 'A'
        userFriend1.save()
        UserFriends.objects.create(user=friend, friend=userObj, approvalStatus='A').save()
        return HttpResponseRedirect('/core/')


@login_required
@csrf_exempt
def rejectUser(request):
    if request.is_ajax():
        friend = User.objects.get(id=request.POST['id'])
        friendObj = UserInfo.objects.get(user=friend)
        user = request.user.id
        userFriend1 = UserFriends.objects.get(user=user, friend=friendObj)
        userFriend1.delete()
        return HttpResponseRedirect('/core/')


@login_required
def eventMap(request):
    if request.method == 'GET':
        token = {}
        token = dict()
        token['location'] = request.user.id
        return render_to_response("core/eventMap.html", token)


@login_required
def profileView(request):
    if request.method == 'GET':
        token = {}
        token = dict()
        token['id'] = request.user.id
        return render_to_response("core/userProfile.html", token)


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


@api_view(['GET'])
def userFriends(request, pk):
    if request.method == 'GET':
        user = User.objects.get(id=pk)
        userObj = UserFriends.objects.filter(user=user)
        serialize = UserFriendsSerializer(userObj, many=True)
        print(serialize.data)
        return Response(serialize.data)


@api_view(['GET'])
def searchUsers(request, searchStr):
    if request.method == 'GET':
        userObj = UserInfo.objects.filter(
            Q(user__username__contains=searchStr) |
            Q(user__first_name__contains=searchStr))
        serialize = UserInfoSerializer(userObj, many=True)
        return Response(serialize.data)


@login_required
def userFriendsView(request):
    token = {'fullname': request.user, 'userId': request.user.id}
    return render_to_response("core/friends.html", token)


@login_required
@csrf_exempt
def search(request):
    if request.method == 'POST':
        context = {'searchStr': request.POST['searchStr']}
        return render_to_response("core/search.html", context)
