from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('index/create', views.create),
    path('success', views.success),
    path('logout', views.logout)
]