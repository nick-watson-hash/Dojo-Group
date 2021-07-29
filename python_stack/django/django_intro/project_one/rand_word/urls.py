from django.urls import path
from . import views

urlpatterns =[
    path('', views.index),
    path('random-word', views.random_word),
    path('reset', views.reset)
]