from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    word = get_random_string(length=14)
    request.session['random_word'] = word
    if "counter" not in request.session:
        request.session ['counter'] = 0
        request.session['word_list'] =[]
    request.session ['counter'] += 1
    
    if request.session['random_word']:
        request.session['word_list'].append(word)
    
    
    return render(request, "index.html")

def random_word(request):
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')