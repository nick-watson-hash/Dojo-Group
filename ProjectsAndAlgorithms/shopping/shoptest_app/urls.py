from django.urls import path
from . import views

app_name = 'shoptest_app'

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('index', views.allProdCat),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),

]