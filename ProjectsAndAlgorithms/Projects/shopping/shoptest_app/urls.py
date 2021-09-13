from django.urls import path
from . import views

app_name = 'shop_app'

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProdCatDetail, name='ProdCatDetail'),
    path('search', views.searchProducts, name='search_products'),
    path('login', views.loginPage, name='login_page'),
    path('logout', views.logOut, name='log_out'),
]