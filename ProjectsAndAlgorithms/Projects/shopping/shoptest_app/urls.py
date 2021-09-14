from django.urls import path
from . import views

app_name = 'shop_app'

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProdCatDetail, name='ProdCatDetail'),
    path('search', views.searchProducts, name='search_products'),
    path('register', views.registrationPage, name='registration_page'),
    path('create', views.createAccount, name='account_creation'),
    path('login', views.loginPage, name='login_page'),
    path('sign_in', views.signIn, name='sign_in'),
    path('logout', views.logOut, name='log_out'),
    path('profile', views.profilePage, name='profile'),
    path('update', views.editProfile, name='update'),
    path('delete', views.accountDelete, name='delete'),
]