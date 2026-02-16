from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
    path('signup/guest/', views.signup_guest, name='signup_guest'),
    path('sports/', views.sport_list, name='sport_list'),
    path('sports/create/', views.sport_create, name='sport_create'),
    path('sports/<int:pk>/edit/', views.sport_update, name='sport_update'),
    path('sports/<int:pk>/delete/', views.sport_delete, name='sport_delete'),
    path('tournaments/', views.tournament_list, name='tournament_list'),
    path('tournaments/create/', views.tournament_create, name='tournament_create'),
    path('tournaments/<int:pk>/edit/', views.tournament_update, name='tournament_update'),
    path('tournaments/<int:pk>/delete/', views.tournament_delete, name='tournament_delete'),
    path('teams/', views.team_list, name='team_list'),
    path('teams/create/', views.team_create, name='team_create'),
    path('teams/<int:pk>/edit/', views.team_update, name='team_update'),
    path('teams/<int:pk>/delete/', views.team_delete, name='team_delete'),
    path('players/', views.player_list, name='player_list'),
    path('players/create/', views.player_create, name='player_create'),
    path('players/<int:pk>/edit/', views.player_update, name='player_update'),
    path('players/<int:pk>/delete/', views.player_delete, name='player_delete'),
    path('matches/', views.match_list, name='match_list'),
    path('matches/create/', views.match_create, name='match_create'),
    path('matches/<int:pk>/edit/', views.match_update, name='match_update'),
    path('matches/<int:pk>/delete/', views.match_delete, name='match_delete'),
    path('matches/<int:pk>/result/', views.match_result_update, name='match_result_update'),
    path('create_referee/', views.create_referee, name='create_referee'),
    path('create-captain/', views.create_captain, name='create_captain'),
    path('points-table/<int:tournament_id>/', views.points_table, name='points_table'),

]
