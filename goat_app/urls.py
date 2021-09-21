from django.urls import path
from . import views

urlpatterns=[
    path('', views.landing_page),
    path('create_user', views.create_user),
    path('sign_in', views.sign_in),
    path('first_index', views.first_index),
    path('random_match', views.random_match),
    path('second_index', views.second_index),
    path('run_bet_random', views.run_bet_random),
    path('run_bet_custom', views.run_bet_custom),
    path('winner_page', views.winner_page),
    path('random_winner_page', views.winner_page),
    path('logout', views.logout),
]