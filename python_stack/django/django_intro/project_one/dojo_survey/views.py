from django.shortcuts import render, redirect

language = ['English', 'Spanish', 'German', 'French']
location = ['North', 'South', 'East', 'West']

def index(request):
    context={
        'languages': language,
        'locations': location
    }
    return render(request, "index.html", context)

def result(request):
    return render(request, "result.html")

def process(request):
    if request.method != "POST":
        return redirect('/')
    request.session['first_name']=request.POST['first_name']
    request.session['location']=request.POST['location']
    request.session['language']=request.POST['language']
    return redirect('/result')
# Create your views here.