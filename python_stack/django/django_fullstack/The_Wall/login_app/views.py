from django.shortcuts import render, redirect
from django.contrib import messages
from login_app.models import *
import bcrypt
# Create your views here.

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method != 'POST':
        return redirect('/')
    print(request.POST)
    errors = Users.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/index')
    else:
        new_password = request.POST['password']
        new_passwordHash = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
        new_user = Users.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            date_of_birth = request.POST['date_of_birth'],
            password = new_passwordHash,
        )
        return redirect('/success')

def success(request):
    if 'users_id' not in request.session:
        return redirect('/')
    recentUser = Users.objects.last().first_name
    context = {
        'all_users' : Users.objects.all(),
        'last_user' : recentUser
    }
    messages.success(request, "Successfully registered (or logged in)")
    return render(request, 'success.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')
