from django.shortcuts import render, redirect
import random
from datetime import datetime

gold_total = {
    "farm": (10, 20),
    "cave": (5, 10),
    "house": (2, 5),
    "casino": (0, 50)
}

# Create your views here.
def index(request):
    if not "counter" in request.session or "activities" not in request.session:
        request.session['counter'] = 0
        request.session['activities'] = []
    return render(request, "index.html")
    
def process(request):
    if request.method != "POST":
        return redirect('/')
    building_name = request.POST['building']
    building = gold_total[building_name]
    building_name_upper = building_name[0].upper() + building_name[1:] 
    curr_gold = random.randint(building[0], building[1])
    now_formatted = datetime.now().strftime("%m/%d/%Y %I:%M%p")
    result = 'earn'
    message = f"Earned {curr_gold} from the {building_name_upper}! ({now_formatted})"
    if building_name == 'casino':
        if random.randint(0,1) > 0: 
            message = f"Entered a {building_name_upper} and lost {curr_gold} golds... Ouch... ({now_formatted})"
            curr_gold = curr_gold * -1
    request.session['counter'] += curr_gold
    return redirect('/')