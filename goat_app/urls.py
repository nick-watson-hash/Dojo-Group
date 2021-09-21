from django.urls import path
from . import views

urlpatterns=[
    path('', views.landing_page),
    path('results', views.results),
    # path('pick', views.pick),
    path('create_user', views.create_user),
    path('logout', views.logout),
    path('sign_in', views.sign_in),
    path('player_search', views.player_search),
    path('create', views.create),
    path('add_goat', views.add_goat),
    path('submit', views.submit),
    path('run_bet', views.run_bet),
    path('winner_page', views.winner_page),
    path('matchup_maker', views.matchup_maker),
    path('matchup_picker', views.matchup_picker),
    path('random_match', views.random_match),
    path('stats_comp', views.stats_comp)
]