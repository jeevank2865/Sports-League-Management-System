from django import forms
from .models import Player, Team, Match, CustomUser, Sport, Tournament
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

# USER FORMS
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class GuestSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email']

# BASIC FORMS 
class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = ['name']
class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'sport']

# TEAM FORM
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'coach_name', 'tournament', 'captain']
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['captain'].queryset = CustomUser.objects.filter(role='captain')
        if user and user.role == 'captain':
            self.fields.pop('captain')
# PLAYER FORM
class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'age', 'position', 'team']
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.role == 'captain':
            self.fields['team'].queryset = Team.objects.filter(captain=user)

# MATCH FORMS
class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['sport', 'tournament', 'team1', 'team2', 'scheduled_date']
class MatchResultForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['winner', 'team1_score', 'team2_score', 'POM', 'status']
class GuestSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email']
