from django.shortcuts import render,redirect
from django.contrib import messages
import requests, json, random, bcrypt
from .models import User, GOAT, GOATdb, Matchup

# Registration & Login page
def landing_page(request):
    return render(request, "landing_page.html")

def index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    # Check for user_id in session
    login_check = ""
    if 'user_id' in request.session:
        login_check = User.objects.get(id=request.session['user_id'])

    user = User.objects.get(id=request.session['user_id'])
    context={
        'user':user,
        'goats':GOAT.objects.filter(creator=user),
        'current_user':login_check,
        # 'goat1':request.session['goat1'],
        # 'goat2':request.session['goat2'],
        # 'rand_goat1':request.session['g1'],
        # 'rand_goat2':request.session['g2']
    }
    return render(request, 'index.html', context)

def results(request):
    querry=request.POST["search"]
    url = "https://nba-stats4.p.rapidapi.com/players/"

    querystring = {"page":"1","full_name":querry,"per_page":"50"}

    headers = {
        'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
        'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response)
    resp_json=response.json()
    print(resp_json)
    player_id=(resp_json[0]['id'])
    print(player_id)

    url = "https://nba-stats4.p.rapidapi.com/per_game_career_regular_season/"

    headers = {
        'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
        'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
        }

    response = requests.request("GET", url+str(player_id), headers=headers)
    print(response)
    resp_json_stats=response.json()
    print(resp_json_stats)
    player_name=(resp_json[0]['full_name'])
    for key in resp_json_stats:
        print(key, resp_json_stats[key])

    context={
        'player':player_name,
        'stats':resp_json_stats
    }

    return render(request, 'results.html', context)

def submit(request):
    user=User.objects.get(id=request.session['user_id'])
    print(user.first_name)
    user.bet = request.POST['bet']
    user.vote= request.POST['guess']
    user.save()
    print(user.bet)
    print(user.vote)
    print(user.bank)
    return redirect('/')

# def pick(request):
#     user=User.objects.get(id=2)
#     bank=user.bank
#     list = ['cat', 'dog', 'horse']
#     pick=(random.choice(list))
#     print(pick)
#     x = request.POST['guess'] 
#     wager=int(request.POST['bet'])
#     print(wager)
#     if x == pick:
#         user.bank=bank+wager
#         user.save()
#         print(user.bank)
#     else:
#         user.bank=bank-wager
#         user.save()
#         print(user.bank)
#     context={
#         'thing':pick,
#         'balance':user.bank
#     }
#     return render(request,'results.html', context)


# NEED EDGE CASE FOR IF NAME DOES NOT APPEAR IN SEARCH LINE 106
def player_search(request):
    querry=request.POST["search"]
    # if request.POST["search"] == False:
    #     return redirect('index')
    url = "https://nba-stats4.p.rapidapi.com/players/"

    querystring = {"page":"1","full_name":querry,"per_page":"50"}

    headers = {
        'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
        'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response)
    resp_json=response.json()
    print(resp_json)
    player_id=(resp_json[0]['id'])
    print(player_id)

    url = "https://nba-stats4.p.rapidapi.com/per_game_career_regular_season/"

    headers = {
        'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
        'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
        }

    response = requests.request("GET", url+str(player_id), headers=headers)
    print(response)
    resp_json_stats=response.json()
    print(resp_json_stats)
    player_name=(resp_json[0]['full_name'])
    for key in resp_json_stats:
        print(key, resp_json_stats[key])

    context={
        'player':player_name,
        'stats':resp_json_stats
    }
    request.session['current_goat_profile'] = resp_json
    request.session['current_goat_stats'] = resp_json_stats
    return render(request, 'create.html', context)

def create(request):
    user=User.objects.get(id=request.session['user_id'])
    players = GOAT.objects.filter(creator=user)
    context={
        'goats': players,
    }

    return render(request, 'create.html', context)

def add_goat(request):
    user=User.objects.get(id=request.session['user_id'])
    profile=request.session['current_goat_profile']
    print(profile[0]['id'])
    print(profile[0]['first_name'])
    print(profile[0]['last_name'])
    new_goat=GOAT.objects.create(
        first_name=profile[0]['first_name'],
        last_name=profile[0]['last_name'],
        full_name=profile[0]['full_name'],
        api_id=profile[0]['id'],
        creator=user
    )
    return redirect('/create')

def run_bet(request):
    user=User.objects.get(id=request.session['user_id'])
    bank=user.bank
    list = ['cat', 'dog', 'horse']
    pick=(random.choice(list))
    print(pick)
    user.bank = bank+user.bet if user.vote == pick else bank-user.bet
    user.save()
    print(user.bank)
    user.bet = 0
    user.vote = ""
    user.save()
    print(user.bet)
    print(user.vote)
    print(user.bank)
    request.session['winner']=pick
    return redirect("/winner_page")

def winner_page(request):
    context={
        'winner': request.session['winner'],
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'winner_page.html', context)

# Refactored matchup method
def matchup_maker(request):
    player1 = _extracted_from_matchup_maker_2(request, 'player1_goat')
    player2 = _extracted_from_matchup_maker_2(request, 'player2_goat')
    user=User.objects.get(id=request.session['user_id'])
    new_match=Matchup.objects.create(
        goat1_id=player1.id,
        goat2_id=player2.id,
        user=user
    )
    return redirect('/')
# Recursive matchup method
def _extracted_from_matchup_maker_2(request, arg1):
    goat1 = request.POST[arg1]
    print(goat1)
    result = GOAT.objects.get(full_name=goat1)
    print(result.id)
    return result

def matchup_picker(request):
    matches=Matchup.objects.all()
    print(matches)
    match=(random.choice(matches))
    print(match)
    p1=match.goat1_id
    p2=match.goat2_id
    player1=GOAT.objects.get(id=p1).full_name
    player2=GOAT.objects.get(id=p2).full_name
    request.session['goat1']=player1
    request.session['goat2']=player2
    return redirect('/')

def random_match(request):
    pool1=GOATdb.objects.all()
    pool2=GOATdb.objects.all()
    rand_goat1=(random.choice(pool1))
    rand_goat2=(random.choice(pool2))
    rp1=rand_goat1.full_name
    rp2=rand_goat2.full_name
    print(rp1)
    print(rp2)
    request.session['g1']=rp1
    request.session['g2']=rp2
    return redirect('/')

def stats_comp(request):
    goat_list=GOATdb.objects.all()
    player1=(random.choice(goat_list))
    print(player1)
    querry= player1.full_name
    print(querry)
    url = "https://nba-stats4.p.rapidapi.com/players/"

    querystring = {"page":"1","full_name":querry,"per_page":"50"}

    headers = {
        'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
        'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response)
    resp_json=response.json()
    print(resp_json)
    player_id=(resp_json[0]['id'])
    print(player_id)

    url = "https://nba-stats4.p.rapidapi.com/per_game_career_regular_season/"

    headers = {
        'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
        'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
        }

    response = requests.request("GET", url+str(player_id), headers=headers)
    print(response)
    resp_json_stats=response.json()
    print(resp_json_stats)
    player_name=(resp_json[0]['full_name'])
    print(player_name)
    player1_min=resp_json_stats['min']
    player1_fgm_per_game=resp_json_stats['fgm_per_game']
    player1_fga_per_game =resp_json_stats['fga_per_game']
    player1_fg_pct=resp_json_stats['fg_pct']
    player1_fg3m_per_game=resp_json_stats['fg3m_per_game']
    player1_fg3a_per_game=resp_json_stats['fg3a_per_game']
    player1_fg3_pct =resp_json_stats['fg3_pct']
    player1_ftm_per_game =resp_json_stats['ftm_per_game']
    player1_fta_per_game =resp_json_stats['fta_per_game']
    player1_ft_pct=resp_json_stats['ft_pct']
    player1_oreb_per_game =resp_json_stats['oreb_per_game']
    player1_dreb_per_game =resp_json_stats['dreb_per_game']
    player1_reb_per_game =resp_json_stats['reb_per_game']
    player1_ast_per_game =resp_json_stats['ast_per_game']
    player1_stl_per_game =resp_json_stats['stl_per_game']
    player1_blk_per_game =resp_json_stats['blk_per_game']
    player1_pf_per_game =resp_json_stats['pf_per_game']
    player1_pts_per_game =resp_json_stats['pts_per_game']
    print(player1_min)
    print(player1_fg3a_per_game)

    player2=(random.choice(goat_list))
    print(player2)
    querry= player2.full_name
    print(querry)
    url = "https://nba-stats4.p.rapidapi.com/players/"

    querystring = {"page":"1","full_name":querry,"per_page":"50"}

    headers = {
        'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
        'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response)
    resp_json=response.json()
    print(resp_json)
    player_id=(resp_json[0]['id'])
    print(player_id)

    url = "https://nba-stats4.p.rapidapi.com/per_game_career_regular_season/"

    headers = {
        'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
        'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
        }

    response = requests.request("GET", url+str(player_id), headers=headers)
    print(response)
    resp_json_stats=response.json()
    print(resp_json_stats)
    player_name=(resp_json[0]['full_name'])
    print(player_name)
    player2_min=resp_json_stats['min']
    player2_fgm_per_game=resp_json_stats['fgm_per_game']
    player2_fga_per_game =resp_json_stats['fga_per_game']
    player2_fg_pct=resp_json_stats['fg_pct']
    player2_fg3m_per_game=resp_json_stats['fg3m_per_game']
    player2_fg3a_per_game=resp_json_stats['fg3a_per_game']
    player2_fg3_pct =resp_json_stats['fg3_pct']
    player2_ftm_per_game =resp_json_stats['ftm_per_game']
    player2_fta_per_game =resp_json_stats['fta_per_game']
    player2_ft_pct=resp_json_stats['ft_pct']
    player2_oreb_per_game =resp_json_stats['oreb_per_game']
    player2_dreb_per_game =resp_json_stats['dreb_per_game']
    player2_reb_per_game =resp_json_stats['reb_per_game']
    player2_ast_per_game =resp_json_stats['ast_per_game']
    player2_stl_per_game =resp_json_stats['stl_per_game']
    player2_blk_per_game =resp_json_stats['blk_per_game']
    player2_pf_per_game =resp_json_stats['pf_per_game']
    player2_pts_per_game =resp_json_stats['pts_per_game']
    print(player2_min)
    print(player2_fg3a_per_game)
    # player_name=(resp_json[0]['full_name'])
    # player_name=(resp_json[0]['full_name'])
    for key in resp_json_stats:
        print(key, resp_json_stats[key])
    return redirect('/')

# User creation method
def create_user(request):
    if request.method != 'POST':
        return redirect('/')
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        new_password = request.POST['password']
        new_passwordHash = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            hashpass = new_passwordHash,
        )
        request.session['user_id'] = new_user.id

    return redirect('/')

# Registration & Login page
def profile(request):
    return render(request, "profile.html")

# Edit user method
def edit_user(request):
    if 'user_id' not in request.session:
        return redirect('/')
    # Checks for user_id in request.session
    if 'user_id' in request.session:
        profile_edit = User.objects.get(id=request.session['user_id'])
    profile_edit.email = request.POST['email_edit']
    profile_edit.save()
    return redirect('profile')

# Login Method
def sign_in(request):
    if request.method != 'POST':
        return redirect('/')
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/login')
    logged_in = User.objects.filter(username=request.POST['login_username'])
    request.session['user_id'] = logged_in[0].id
    return redirect('index')

# Logout Method
def logout(request):
    request.session.flush()
    return redirect('/')

