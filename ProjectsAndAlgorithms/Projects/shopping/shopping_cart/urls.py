from django.urls import path
from . import views

app_name = 'shopping_cart'

urlpatterns = [
    path('/add/<int:product_id>/', views.addCart, name='add_cart'),
    path('', views.cartDetails, name='cart_details'),
    path('/remove/<int:product_id>/', views.itemRemove, name='item_remove'),
    path('/destroy/<int:product_id>/', views.removeAll, name='remove_all')
]