from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    # path('results', views.results),
    # path('pick', views.pick),
    # path('player_search', views.player_search),
    # path('create', views.create),
    # path('add_goat', views.add_goat),
    # path('submit_custom', views.submit_custom),
    # path('submit_random', views.submit_random),
    path('run_bet_random', views.run_bet_random),
    path('run_bet_custom', views.run_bet_custom),
    path('winner_page', views.winner_page),
    path('random_winner_page', views.winner_page),
    # path('matchup_maker', views.matchup_maker),
    # path('matchup_picker', views.matchup_picker),
    path('random_match', views.random_match),
    # path('stats_comp', views.stats_comp)
]