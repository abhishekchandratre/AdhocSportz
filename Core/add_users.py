from django.contrib.auth import get_user_model
from django.http import HttpResponse
from Core.models import Location, UserInfo, Sports, Events
import datetime
import subprocess


def create_user_with_all_details(request):

    #Run bash script to perform migrations and deletion and insertion of data
    subprocess.call("./scripts/repace_db.sh")

    # Creating Location
    location1 = Location.objects.create(country='India', state='MH',region='Pune')
    location1.save()
    location2 = Location.objects.create(country='United States', state='NC',region='Charlotte')
    location2.save()
    location3 = Location.objects.create(country='United States', state='FL',region='Maimi')
    location3.save()

    User = get_user_model()

    #  Update the users in this list.
    #  Each tuple represents the username, password, and email of a user.
    users = [
        ('user1', 'qwerasdf', 'wermsam92@gmail.com', 'Abhishek', 'Chandratre', 'profile_img/abhishek.jpg'),
        ('user2', 'qwerasdf', 'wermsam92@gmail.com', 'Sampath', 'Kumar', 'profile_img/sampath.jpg'),
        ('user3', 'qwerasdf', 'chinmay811@gmail.com', 'Chinmay', 'Rawool', 'profile_img/chinmay.jpg'),
        ('user4', 'qwerasdf', 'user_3@example.com', 'Sravani', 'Kannelur', 'profile_img/sravani.jpg'),
    ]

    for username, password, email, first_name, last_name, profilePicture in users:
        print('Creating user {0}.'.format(username))
        user = User.objects.create_user(username, email,password)
        user.last_name = last_name
        user.first_name = first_name
        user.save()
        print('User {0} successfully created.'.format(username))
        userInfo = UserInfo(gender='M', user=user, birthDate=datetime.date.today(),
                            phoneNumber='7049068013', oneLinerStatus='Add me',
                            location= location1, profilePicture=profilePicture)
        sport1 = Sports.objects.get(sportName='Skiing')
        sport2 = Sports.objects.get(sportName='Judo')
        sport3 = Sports.objects.get(sportName='Polo')
        userInfo.save()
        userInfo.sports.add(sport1)
        userInfo.sports.add(sport2)
        userInfo.sports.add(sport3)
        userInfo.save()
        events = [
            (user, sport1, 'Skiiiiing Challenge by ' + first_name, 'Winter is coming',
             datetime.date.today(),location1,10,'Public'),
            (user, sport2, 'Private Judo Challenge by ' + first_name, 'Let\'s fight',
             datetime.date.today(),location2,10,'Private'),
            (user, sport3, 'Polo Challenge by ' + first_name, 'Polo Challenge',
             datetime.date.today(),location3,10,'Public')
        ]

        for owner, sport, name, desc, startDate, location, num_player, evt_type in events:
            event = Events(owner=owner,sport=sport,name=name,desc=desc,startDate=startDate,
                           location=location,numberOfPlayers=num_player,eventType=evt_type)
            event.save()

    return HttpResponse("<h1>Added Users</h1>")
