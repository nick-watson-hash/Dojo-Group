from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('wall', views.wall),
    path('index', views.index),
    path('index/create', views.create),
    path('success/', views.success),
    path('success/<int:user_id>', views.success),
    path('success/<int:id>/edit_user', views.edit_user),
    path('logout', views.logout),
    path('login', views.login),
    path('message', views.message),
    path('delete_comment/<int:id>', views.delete_comment),
    path('delete_message/<int:id>', views.delete_message),
    path('wall/<int:id>', views.delete_message_wall),
    path('add_comment/<int:id>', views.post_comment),
]