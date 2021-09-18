from django.shortcuts import render,redirect
import requests, json, random
from .models import User, GOAT, GOATdb, Matchup

def index(request):
    user=User.objects.get(id=2)
    context={
        'user':User.objects.get(id=2),
        'goats':GOAT.objects.filter(creator=user),
        'goat1':request.session['goat1'],
        'goat2':request.session['goat2'],
        'rand_goat1':request.session['g1'],
        'rand_goat2':request.session['g2']
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
    user=User.objects.get(id=2)
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

def player_search(request):
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
    request.session['current_goat_profile'] = resp_json
    request.session['current_goat_stats'] = resp_json_stats
    return render(request, 'create.html', context)

def create(request):
    user=User.objects.get(id=2)
    players = GOAT.objects.filter(creator=user)
    context={
        'goats': players,
    }

    return render(request, 'create.html', context)

def add_goat(request):
    user=User.objects.get(id=2)
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
    user=User.objects.get(id=2)
    bank=user.bank
    list = ['cat', 'dog', 'horse']
    pick=(random.choice(list))
    print(pick)
    if user.vote == pick:
        user.bank=bank+user.bet
        user.save()
        print(user.bank)
    else:
        user.bank=bank-user.bet
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
        'user': User.objects.get(id=2)
    }
    return render(request, 'winner_page.html', context)

def matchup_maker(request):
    goat1=request.POST['player1_goat']
    print(goat1)
    player1=GOAT.objects.get(full_name=goat1)
    print(player1.id)
    goat2=request.POST['player2_goat']
    print(goat2)
    player2=GOAT.objects.get(full_name=goat2)
    print(player2.id)
    user=User.objects.get(id=2)
    new_match=Matchup.objects.create(
        goat1_id=player1.id,
        goat2_id=player2.id,
        user=user
    )
    return redirect('/')

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



