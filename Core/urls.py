from django.conf.urls import url

from . import views

urlpatterns = {
    url(r'^$', views.index, name='index'),
    url(r'register/basic$', views.register, name='register'),
    url(r'register/sportsInterest$', views.sportsInterest, name='sportInterest'),
    url(r'register/userInfo$', views.userInfo, name='userInfo'),
    url(r'accounts/complete$', views.registration_complete, name='register_complete'),
    url(r'accounts/login$', views.login_user, name='login'),
    url(r'accounts/logout$', views.logout_user, name='login'),
}
