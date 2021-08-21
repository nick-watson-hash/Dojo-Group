from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('login', views.login),
    path('logout', views.logout),
    path('createuser', views.createUser),
    path('createbook', views.createBooks),
    path('books', views.books),
    path('books/<int:id>', views.bookinfo),
    path('edit/<int:id>', views.editBook),
    path('delete/<int:id>', views.deleteBook),
    path('favorite/<int:book_id>', views.addFavorite),
    path('unfavorite/<int:book_id>', views.unfavorite)
]
