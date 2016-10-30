from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget
from .models import Sports, UserInfo, UserSportsInterest, Events, Location


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
    username = forms.CharField(max_length=250)
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        strip=False,
    )


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('gender', 'birthDate', 'phoneNumber', 'oneLinerStatus')


class SportsInterestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices')
        super(SportsInterestForm, self).__init__(*args, **kwargs)

        for sport_type in choices:
            self.fields[sport_type] = forms.CharField(
                label=sport_type,
                widget=forms.TextInput(attrs={'readonly': 'readonly'}),
                required=False,
            )
            for sport in choices[sport_type]:
                self.fields[sport_type + sport] = forms.BooleanField(
                    required=False,
                    label=sport,
                )

    def save(self, choices, userInfoObjId):
        for sport_type in choices:
            for sport in choices[sport_type]:
                if (sport_type + sport) in self.data:
                    sportObj = Sports.objects.get(sportName=sport)
                    userSportObj = UserSportsInterest(sport_id=sportObj.id, userInfo_id=userInfoObjId)
                    userSportObj.save()


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('name', 'desc', 'sport', 'startDate', 'location', 'numberOfPlayers')
        widgets = {'startDate': SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    )}


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('country', 'state', 'region')
