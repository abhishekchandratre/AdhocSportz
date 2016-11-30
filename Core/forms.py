from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget
from .models import Sports, UserInfo, Events, Location
from django.forms import extras


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'Username'}),
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        strip=False,
    )


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('gender', 'birthDate', 'phoneNumber', 'oneLinerStatus','profilePicture')
        widgets = {'birthDate': extras.SelectDateWidget(years=range(1970, 2016))}
        #widgets = {'birthDate': forms.DateInput(attrs={'class':'datepicker'})}


class SportsInterestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices')
        super(SportsInterestForm, self).__init__(*args, **kwargs)

        for sport_type in choices:
            for sport in choices[sport_type]:
                self.fields[sport_type + sport] = forms.BooleanField(
                    required=False,
                    label=sport,
                )

    def save(self, choices, userInfoObj):
        userInfoObj.save()
        for sport_type in choices:
            for sport in choices[sport_type]:
                if (sport_type + sport) in self.data:
                    sportObj = Sports.objects.get(sportName=sport)
                    userInfoObj.sports.add(sportObj)
        userInfoObj.save()


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('name', 'desc', 'sport', 'startDate', 'numberOfPlayers', 'eventType')
        widgets = {'startDate': extras.SelectDateWidget(years=range(2016, 2020))}

    def save(self,commit=True):
        event = super(EventForm, self).save(commit=False)
        if commit:
            event.save()
        return event


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('country', 'state', 'region')

