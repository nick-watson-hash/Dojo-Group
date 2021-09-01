from django.shortcuts import render, redirect
from django.contrib import messages
from books_app.models import *
import bcrypt


def index(request):
    request.session.flush()
    return render(request, 'index.html')

def books(request):
    context = {
        'all_users' : User.objects.all(),
        'all_books' : Book.objects.all(),
        'currentUser' : User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'books.html', context)

def bookinfo(request, id):
    context = {
        'specific_book' : Book.objects.get(id = id),
    }
    return render(request, 'bookinfo.html', context)

def favoriteList(request, id):
    context = {
        'specific_user' : User.objects.get(id = id)
    }
    return render(request, 'user.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

def login(request):
    if request.method != 'POST':
        return redirect('/')
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    logged_in = User.objects.filter(email=request.POST['login_email'])
    request.session['user_id'] = logged_in[0].id
    request.session['first_name'] = logged_in[0].first_name
    return redirect('/books')

def createUser(request):
    if request.method != 'POST':
        return redirect('/')
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        new_password = request.POST['password']
        new_passwordHash = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = new_passwordHash,
        )
        logged_in = User.objects.filter(email=request.POST['email'])
        request.session['user_id'] = logged_in[0].id
        request.session['first_name'] = logged_in[0].first_name
        return redirect('/books')

def createBooks(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    else:
        currentUser = User.objects.get(id=request.session['user_id'])
        new_book = Book.objects.create(
            title = request.POST['bookTitle'],
            desc = request.POST['bookDescription'],
            creator = currentUser
        )
        currentUser.fav_book.add(new_book)
        currentUser.liked_book.add(new_book)
    return redirect('/books')

def deleteBook(request, id):
    destroy = Book.objects.get(id=id)
    destroy.delete()
    return redirect('/books')

def editBook(request, id):
    errors = Book.objects.edit_validator(request.POST)
    edit_book = Book.objects.get(id=id)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/books/{edit_book.id}')
    edit_book.desc = request.POST['bookDescriptionEdit']
    edit_book.save()
    return redirect(f'/books/{edit_book.id}')

def addFavorite (request, book_id):
    currentUser = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id = book_id)
    currentUser.liked_book.add(book)
    return redirect(f'/books/{book_id}')

def unfavorite(request, book_id):
    currentUser = User.objects.get(id=request.session["user_id"])
    book = Book.objects.get(id=book_id)
    currentUser.liked_book.remove(book)
    return redirect(f'/books/{book_id}')
