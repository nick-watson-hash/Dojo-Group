from django.shortcuts import render, redirect
from django.contrib import messages
from semi_rest_prac_app.models import *


def index(request):
    context = {
        'all_shows' : Shows.objects.all()
    }
    return render(request, "index.html", context)

def new_show(request):
        return render(request, "new_show.html") 

def create_show(request):
    if request.method != "POST":
        return redirect('/')

    errors = Shows.objects.basic_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
            messages.success(request, "Show unsuccessfully created")
        return redirect('new')

    else:
        new_show = Shows.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            desc = request.POST['desc']
            )
        return redirect (f'/shows/{new_show.id}')

def show_profile(request, show_id):
    queried_show = Shows.objects.get(id = show_id)
    context = {
        'queried_show' : queried_show
    }
    return render(request, "show_profile.html", context)

def edit_show(request, show_id):

    queried_show = Shows.objects.get(id = show_id)
    context = {
        'queried_show' : queried_show
    }
    return render(request, 'edit_show.html', context)

def update_show(request, show_id):
    if request.method != "POST":
        return redirect('/')

    errors = Shows.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')
    else:
        show = Shows.objects.get(id = show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.desc = request.POST['desc']
        show.save()
        messages.success(request, "Show successfully updated")
        return redirect(f'/shows/{show_id}')

def destroy(request, show_id):
        willdelete = Shows.objects.get(id=show_id)
        willdelete.delete()
        return redirect('/')