from django.shortcuts import render, redirect
from django.contrib import messages
from wall_app.models import *
import bcrypt
# Create your views here.

def wall(request):
    context = {
        'wall_messages' : Message.objects.all(),
    }
    return render(request, 'wall.html', context)

def index(request):
    request.session.flush()
    return render(request, 'index.html')

def create(request):
    if request.method != 'POST':
        return redirect('/')
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
        request.session['user_id'] = new_user.id
        return redirect(f'/success/{new_user.id}')

def success(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/')
    recentUser = Users.objects.get(id = request.session['user_id'])
    context = {
        'all_users' : Users.objects.all(),
        'last_user' : recentUser,
        'user_messages' : Message.objects.filter(user = Users.objects.get(id=request.session['user_id']))
    }
    messages.success(request, "Successfully registered (or logged in)")
    return render(request, 'success.html', context)

def login(request):
    errors = Users.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/index')
    logged_in = Users.objects.filter(email=request.POST['login_email'])
    request.session['user_id'] = logged_in[0].id
    request.session['first_name'] = logged_in[0].first_name
    return redirect(f'/success/{logged_in[0].id}')

def logout(request):
    request.session.flush()
    return redirect('/')

def message(request):
    Message.objects.create(message=request.POST['message'], user=Users.objects.get(id=request.session['user_id']))
    return redirect(f"/success/{request.session['user_id']}")

def post_comment(request, id):
    poster = Users.objects.get(id=request.session['user_id'])
    message = Message.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], user=poster, message=message)
    return redirect('/wall')

def delete_comment(request, id):
    destroy = Comment.objects.get(id=id)
    destroy.delete()
    return redirect('/wall')

def delete_message(request, id):
    destroy = Message.objects.get(id=id)
    destroy.delete()
    return redirect('/wall')