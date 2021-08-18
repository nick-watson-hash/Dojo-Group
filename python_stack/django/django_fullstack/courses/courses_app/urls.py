from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('courses', views.index, name='home'),
    path('courses/add', views.add_course),
    path('courses/destroy/<int:course_id>', views.destroy),
    path('courses/destroy/<int:course_id>/delete', views.delete,)
]