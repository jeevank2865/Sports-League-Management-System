from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from .models import CustomUser, Sport, Tournament, Team, Player, Match
from .forms import (
    GuestSignupForm, SportForm, TournamentForm, TeamForm,
    PlayerForm, MatchForm, MatchResultForm, CustomUserCreationForm
)

from collections import defaultdict
from django.contrib.auth import authenticate


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard') 
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'tournament/login.html')


# Home View
def home(request):
    return render(request, 'tournament/home.html')


# Guest Signup
def signup_guest(request):
    if request.method == 'POST':
        form = GuestSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'guest'
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = GuestSignupForm()
    return render(request, 'tournament/signup_guest.html', {'form': form})


# Dashboard by Role
@login_required
def dashboard(request):
    role = request.user.role
    if role == 'admin':
        return render(request, 'tournament/admin_dashboard.html')
    elif role == 'captain':
        team = Team.objects.filter(captain=request.user).first()
        tournament = Tournament.objects.first()
        return render(request, 'tournament/captain_dashboard.html', {
            'team': team,
            'tournament': tournament,
        })
    elif role == 'referee':
        tournament = Tournament.objects.first()
        return render(request, 'tournament/referee_dashboard.html', {
        'tournament': tournament
    })
    else:
        tournaments = Tournament.objects.all()
        return render(request, 'tournament/guest_dashboard.html', {'tournaments': tournaments})


# Admin/Captain Check
def is_admin_or_captain(user):
    return user.role in ['admin', 'captain']


# Admin Check
def is_admin(user):
    return user.role == 'admin'


# Referee or Admin Check
def is_admin_or_referee(user):
    return user.role in ['admin', 'referee']


# ---------- SPORT VIEWS ----------
@login_required
def sport_list(request):
    sports = Sport.objects.all()
    return render(request, 'tournament/sport_list.html', {'sports': sports})


@login_required
def sport_create(request):
    form = SportForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('sport_list')
    return render(request, 'tournament/sport_form.html', {'form': form})


@login_required
def sport_update(request, pk):
    sport = get_object_or_404(Sport, pk=pk)
    form = SportForm(request.POST or None, instance=sport)
    if form.is_valid():
        form.save()
        return redirect('sport_list')
    return render(request, 'tournament/sport_form.html', {'form': form})


@login_required
def sport_delete(request, pk):
    sport = get_object_or_404(Sport, pk=pk)
    if request.method == 'POST':
        sport.delete()
        return redirect('sport_list')
    return render(request, 'tournament/sport_confirm_delete.html', {'object': sport})


# TOURNAMENT VIEWS 
@login_required
def tournament_list(request):
    tournaments = Tournament.objects.select_related('sport').all()
    return render(request, 'tournament/tournament_list.html', {'tournaments': tournaments})


@login_required
def tournament_create(request):
    form = TournamentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tournament_list')
    return render(request, 'tournament/tournament_form.html', {'form': form})


@login_required
def tournament_update(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    form = TournamentForm(request.POST or None, instance=tournament)
    if form.is_valid():
        form.save()
        return redirect('tournament_list')
    return render(request, 'tournament/tournament_form.html', {'form': form})


@login_required
def tournament_delete(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    if request.method == 'POST':
        tournament.delete()
        return redirect('tournament_list')
    return render(request, 'tournament/tournament_confirm_delete.html', {'object': tournament})


# TEAM VIEWS
@login_required
def team_list(request):
    teams = Team.objects.select_related('tournament').all()
    return render(request, 'tournament/team_list.html', {'teams': teams})


@login_required
@user_passes_test(is_admin_or_captain)
def team_create(request):
    form = TeamForm(request.POST or None, user=request.user)
    if form.is_valid():
        team = form.save(commit=False)
        team.captain = request.user
        team.save()
        return redirect('team_list')
    return render(request, 'tournament/team_form.html', {'form': form})


@login_required
@user_passes_test(is_admin_or_captain)
def team_update(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.user.role != 'admin' and request.user != team.captain:
        return redirect('team_list')
    form = TeamForm(request.POST or None, instance=team, user=request.user)
    if form.is_valid():
        form.save()
        return redirect('team_list')
    return render(request, 'tournament/team_form.html', {'form': form})


@login_required
@user_passes_test(is_admin_or_captain)
def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.user.role != 'admin' and request.user != team.captain:
        return redirect('team_list')
    if request.method == 'POST':
        team.delete()
        return redirect('team_list')
    return render(request, 'tournament/team_confirm_delete.html', {'object': team})


# PLAYER VIEWS 
@login_required
def player_list(request):
    user = request.user
    if user.role == 'admin' or user.role == 'referee' or user.role == 'guest':
        players = Player.objects.select_related('team', 'team__tournament').all()

    elif user.role == 'captain':
        players = Player.objects.filter(team__captain=user).select_related(
            'team', 'team__tournament'
        )

    else:
        players = Player.objects.none()

    return render(request, 'tournament/player_list.html', {'players': players})

@login_required
@user_passes_test(is_admin_or_captain)
def player_create(request):
    form = PlayerForm(request.POST or None, user=request.user)

    if request.user.role == 'captain':
        form.fields['team'].queryset = Team.objects.filter(captain=request.user)

    if form.is_valid():
        player = form.save(commit=False)
        if request.user.role == 'captain' and player.team.captain != request.user:
            messages.error(request, "You can add players only to your own team.")
            return redirect('player_list')

        player.save()
        return redirect('player_list')

    return render(request, 'tournament/player_form.html', {'form': form})

@login_required
@user_passes_test(is_admin_or_captain)
def player_update(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.user.role == 'captain' and player.team.captain != request.user:
        return redirect('player_list')
    form = PlayerForm(request.POST or None, instance=player, user=request.user)
    if form.is_valid():
        form.save()
        return redirect('player_list')
    return render(request, 'tournament/player_form.html', {'form': form})


@login_required
@user_passes_test(is_admin_or_captain)
def player_delete(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.user.role == 'captain' and player.team.captain != request.user:
        return redirect('player_list')
    if request.method == 'POST':
        player.delete()
        return redirect('player_list')
    return render(request, 'tournament/player_confirm_delete.html', {'object': player})


# MATCH VIEWS
@login_required
def match_list(request):
    matches = Match.objects.select_related('sport', 'tournament', 'team1', 'team2').all()
    return render(request, 'tournament/match_list.html', {'matches': matches})


@login_required
@user_passes_test(is_admin)
def match_create(request):
    form = MatchForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('match_list')
    return render(request, 'tournament/match_form.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def match_update(request, pk):
    match = get_object_or_404(Match, pk=pk)
    form = MatchForm(request.POST or None, instance=match)
    if form.is_valid():
        form.save()
        return redirect('match_list')
    return render(request, 'tournament/match_form.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def match_delete(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == 'POST':
        match.delete()
        return redirect('match_list')
    return render(request, 'tournament/match_confirm_delete.html', {'object': match})


# MATCH RESULT 
@login_required
@user_passes_test(is_admin_or_referee)
def match_result_update(request, pk):
    match = get_object_or_404(Match, pk=pk)

    if request.method == 'POST':
        form = MatchResultForm(request.POST, instance=match)
    else:
        form = MatchResultForm(instance=match)

    form.fields['winner'].queryset = Team.objects.filter(
        id__in=[match.team1_id, match.team2_id]
    )

    form.fields['POM'].queryset = Player.objects.filter(
        team__in=[match.team1, match.team2]
    )

    if form.is_valid():
        match = form.save(commit=False)

        if match.team1_score is not None and match.team2_score is not None:
            if match.team1_score > match.team2_score:
                match.result = f"{match.team1.name} won"
            elif match.team2_score > match.team1_score:
                match.result = f"{match.team2.name} won"
            else:
                match.result = "Match Draw"

        match.status = 'completed'
        match.save()

        return redirect('dashboard')

    return render(request, 'tournament/match_result_form.html', {
        'form': form,
        'match': match
    })
   # POINTS TABLE
from collections import defaultdict
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tournament, Match

@login_required
def points_table(request, tournament_id=None):
    """
    Show points table for a tournament.
    - If tournament_id is given and valid, show that tournament.
    - If tournament_id is missing or invalid, redirect to first tournament (if any).
    - If no tournaments, redirect to tournament list with an error message.
    """
    tournaments = Tournament.objects.all().order_by('id')

    if not tournaments.exists():
        messages.error(request, "No tournaments found. Please create one first.")
        return redirect('tournament_list')

    if tournament_id is None:
        tournament = tournaments.first()
        return redirect('points_table', tournament_id=tournament.id)
    else:
        tournament = Tournament.objects.filter(pk=tournament_id).first()
        if not tournament:
            first_t = tournaments.first()
            return redirect('points_table', tournament_id=first_t.id)

    matches = Match.objects.filter(tournament=tournament).exclude(
        team1_score__isnull=True, team2_score__isnull=True
    )
    table = defaultdict(lambda: {'played': 0, 'won': 0, 'draw': 0, 'lost': 0, 'points': 0})

    for match in matches:
        team1 = match.team1.name
        team2 = match.team2.name
        score1 = match.team1_score
        score2 = match.team2_score

        table[team1]['played'] += 1
        table[team2]['played'] += 1

        if score1 > score2:
            table[team1]['won'] += 1
            table[team1]['points'] += 3
            table[team2]['lost'] += 1
        elif score2 > score1:
            table[team2]['won'] += 1
            table[team2]['points'] += 3
            table[team1]['lost'] += 1
        else:
            table[team1]['draw'] += 1
            table[team2]['draw'] += 1
            table[team1]['points'] += 1
            table[team2]['points'] += 1

    sorted_table = sorted(table.items(), key=lambda x: (x[1]['points'], x[1]['won']), reverse=True)

    return render(request, 'tournament/points_table.html', {
        'points': sorted_table,
        'tournament': tournament,
        'tournaments': tournaments,
    })

# CREATE CAPTAIN/REFEREE
User = get_user_model()

def create_captain(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            captain = form.save(commit=False)
            captain.role = 'captain'
            captain.save()
            group, created = Group.objects.get_or_create(name='Captain')
            captain.groups.add(group)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'tournament/create_captain.html', {'form': form})


@login_required
def create_referee(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            referee = form.save(commit=False)
            referee.role = 'referee'
            referee.save()
            group, _ = Group.objects.get_or_create(name='Referee')
            referee.groups.add(group)
            messages.success(request, "Referee account created successfully.")
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'tournament/create_referee.html', {'form': form})
