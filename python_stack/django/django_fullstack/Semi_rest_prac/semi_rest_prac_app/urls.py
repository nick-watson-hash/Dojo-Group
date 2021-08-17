from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.index),
    path('shows/new', views.new_show, name='new'),
    path('shows/create', views.create_show),
    path('shows/<int:show_id>', views.show_profile,),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('shows/<int:show_id>/update', views.update_show),
    path('shows/<int:show_id>/destroy', views.destroy)
]