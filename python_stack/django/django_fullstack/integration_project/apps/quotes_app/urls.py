from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('success', views.success),
    path('createuser', views.createUser),
    path('login', views.login),
    path('logout', views.logout),
    path('quotes/', views.wall),
    path('quotes/<int:id>', views.edit),
    path('quotes/<int:id>/edit', views.editQuote),
    path('createquotes', views.createQuote),
    path('delete/<int:id>', views.deleteQuote),
    path('favorite/<int:quote_id>', views.addFavorite),
    path('unfavorite/<int:quote_id>', views.unfavorite),
    path('users/<int:id>', views.users)

]