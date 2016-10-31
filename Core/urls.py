from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register/basic$', views.registerBasic, name='register'),
    url(r'register/sportsInterest$', views.registersSportsInterest, name='sportInterest'),
    url(r'register/userInfo$', views.registerUserInfo, name='userInfo'),
    url(r'register/eventCreate$', views.eventCreate, name='eventCreate'),
    url(r'accounts/complete$', views.registration_complete, name='register_complete'),
    url(r'login/complete$', views.homePage, name='homepage'),
    url(r'accounts/login$', views.login_user, name='login'),
    url(r'accounts/logout$', views.logout_user, name='login'),
    url(r'accounts/profile$', views.profileView, name='profile'),
    url(r'api/sports/$',views.sportCollection,name='sportCollection'),
    url(r'api/user/$',views.userCollection,name='userCollection'),
    url(r'api/user/(?P<pk>[0-9]+)/$',views.userDetails,name='userCollection'),
]
