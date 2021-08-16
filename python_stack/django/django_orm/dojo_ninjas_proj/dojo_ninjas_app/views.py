from django.shortcuts import render, redirect
from dojo_ninjas_app.models import *

# Create your views here.
def index(request):
    context = {
        'all_ninjas' : Ninjas.objects.all(),
        'all_dojos' : Dojos.objects.all()
    }
    return render(request, 'index.html', context)

def process_ninja(request):
    if request.method != 'POST':
        return redirect('/')
    else:
        Ninjas.objects.create(
            first_name = request.POST['ninja_first'],
            last_name = request.POST['ninja_last'],
            dojo_id = request.POST['ninja_dojo']
        )
        return redirect('/')

def process_dojo(request):
    if request.method != 'POST':
        return redirect('/')
    else:
        Dojos.objects.create(
            name = request.POST['dojo_name'] ,
            city = request.POST['dojo_city'],
            state = request.POST['dojo_state']
        )
        return redirect('/')