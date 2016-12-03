from django.conf.urls import url

from . import views
from . import add_users

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register/basic$', views.registerBasic, name='register'),
    url(r'register/sportsInterest$', views.registersSportsInterest, name='sportInterest'),
    url(r'register/userInfo$', views.registerUserInfo, name='userInfo'),
    url(r'register/eventCreate$', views.eventCreate, name='eventCreate'),
    url(r'register/eventView$', views.eventView, name='eventView'),
    url(r'register/eventApprove$', views.eventApprove, name='eventApprove'),
    url(r'accounts/complete$', views.registration_complete, name='register_complete'),
    url(r'login/complete$', views.homePage, name='homepage'),
    url(r'accounts/login$', views.login_user, name='login'),
    url(r'accounts/logout$', views.logout_user, name='login'),
    url(r'event/join$', views.eventJoin, name='eventJoin'),
    url(r'event/approve$', views.eventApproval, name='eventApproval'),
    url(r'user/connect$', views.connect, name='connect'),
    url(r'user/accept$', views.acceptUser, name='acceptUser'),
    url(r'user/reject$', views.rejectUser, name='rejectUser'),
    url(r'accounts/profile$', views.profileView, name='profile'),
    url(r'accounts/friendsProfile/(?P<pk>[0-9]+)/$', views.friendsprofileView, name='friendsProfile'),
    url(r'api/sports/$', views.sportCollection, name='sportCollection'),
    url(r'api/user/$', views.userCollection, name='userCollection'),
    url(r'api/user/(?P<pk>[0-9]+)/$', views.userDetails, name='userDetails'),
    url(r'api/myevent/$', views.myEventCollection, name='myEventCollection'),
    url(r'api/eventMap/$', views.eventMap, name='eventMap'),
    url(r'api/event/$', views.eventCollection, name='eventCollection'),
    url(r'api/privateEvent/$', views.privateEventCollection, name='privateEventCollection'),
    url(r'api/publicEvent/$', views.publicEventCollection, name='publicEventCollection'),
    url(r'api/event/(?P<pk>[0-9]+)/$', views.eventDetails, name='eventDetails'),
    url(r'api/friends/(?P<pk>[0-9]+)/$', views.userFriends, name='userFriends'),
    url(r'api/searchUsers/(?P<searchStr>[0-9a-zA-Z]+)/$', views.searchUsers, name='searchUsers'),
    url(r'add_users/$', add_users.create_user_with_all_details, name='eventCollection'),
    url(r'friends/$', views.userFriendsView, name='eventCollection'),
    url(r'search/$', views.search, name='searchUsers'),
]
