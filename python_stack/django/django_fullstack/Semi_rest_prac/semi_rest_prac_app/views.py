from django.shortcuts import render, redirect
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
        else:
            new_show = Shows.objects.create(
                title = request.POST['title'],
                network = request.POST['network'],
                release_date = request.POST['release_date'],
                desc = request.POST['desc']
                )
            print(new_show.id)
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
    return render(request, f'shows/{queried_show.id}/edit', context)

def update_show(request, show_id):
        if request.method != "POST":
                return redirect('/')
        else:
                updated = Shows.objects.get(id=show_id)
                updated.title = request.POST['title'],
                updated.network = request.POST['network'],
                updated.release_date = request.POST['release_date'],
                updated.desc = request.POST['desc']
                updated.save()
        return redirect('/show_profile.html')

def destroy(request, show_id):
        willdelete = Shows.objects.get(id=show_id)
        willdelete.delete()
        return redirect('/')