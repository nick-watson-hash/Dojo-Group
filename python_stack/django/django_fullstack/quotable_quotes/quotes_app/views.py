from django.shortcuts import render, redirect
from django.contrib import messages
from quotes_app.models import *
import bcrypt


def index(request):
    request.session.flush()
    return render(request, 'index.html')

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
    return redirect('/success')

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
        return redirect('/success')

def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'all_users' : User.objects.all(),
        'all_quotes' : Quote.objects.all(),
        'currentUser' : User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'wall.html', context)

def users(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'specific_user' : User.objects.get(id = id)
    }
    return render(request, 'users.html', context)

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    messages.success(request, "Successfully registered (or logged in)")
    return render(request, 'success.html')

def edit(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'specific_quote' : Quote.objects.get(id = id)
    }
    return render(request, 'edit.html', context)

def createQuote(request):
    errors = Quote.objects.quote_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/quotes')
    else:
        currentUser = User.objects.get(id=request.session['user_id'])
        new_quote= Quote.objects.create(
            author = request.POST['quoteAuthor'],
            desc = request.POST['quoteMessage'],
            creator = currentUser
        )
        currentUser.quote_creator.add(new_quote)
        currentUser.fav_quotes.add(new_quote)
    return redirect('/quotes')

def deleteQuote(request, id):
    destroy = Quote.objects.get(id=id)
    destroy.delete()
    return redirect('/quotes')

def editQuote(request, id):
    errors = Quote.objects.edit_validator(request.POST)
    edit_quote = Quote.objects.get(id=id)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/quotes/{edit_quote.id}')
    edit_quote.author = request.POST['quoteAuthorEdit']
    edit_quote.desc = request.POST['quoteMessageEdit']
    edit_quote.save()
    return redirect(f'/quotes/{edit_quote.id}')

def addFavorite (request, quote_id):
    currentUser = User.objects.get(id=request.session['user_id'])
    quote = Quote.objects.get(id = quote_id)
    currentUser.fav_quotes.add(quote)
    return redirect('/quotes')

def unfavorite(request, quote_id):
    currentUser = User.objects.get(id=request.session["user_id"])
    quote = Quote.objects.get(id=quote_id)
    currentUser.fav_quotes.remove(quote)
    return redirect('/quotes')
