from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('wall', views.wall),
    path('index', views.index),
    path('index/create', views.create),
    path('success', views.success),
    path('logout', views.logout),
    path('login', views.login),
    path('message', views.message),
    path('comment', views.comment),
    path('delete', views.delete),
]