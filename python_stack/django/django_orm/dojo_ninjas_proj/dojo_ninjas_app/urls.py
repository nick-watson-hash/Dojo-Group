from django.urls import path
from . import views	
                    
urlpatterns = [
    path('', views.index),
    path('process-ninja', views.process_ninja),
    path('process-dojo', views.process_dojo)
]