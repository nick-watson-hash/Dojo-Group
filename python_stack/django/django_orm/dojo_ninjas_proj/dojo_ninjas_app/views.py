from django.shortcuts import render, redirect
from dojo_ninjas_app.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html',{'table_data': Ninjas.objects.all()})

def process(request):
    if request.method != 'POST':
        return redirect('/')
    elif request.method == 'POST':
        Ninjas.objects.create(
            first_name = request.POST['one'],
            last_name = request.POST['two'],
            email_address = request.POST['three'],
            years_old = request.POST['four'],
        )
        return redirect('/')