from django.shortcuts import render,redirect
import requests, json, random
from .models import User, GOAT, GOATdb, Matchup

def index(request):
    user=User.objects.get(id=2)
    context={
        'user':User.objects.get(id=2),
        'goats':GOATdb.objects.all(),
        'goat1':request.session['goat1'],
        'goat2':request.session['goat2'],
        'rand_goat1':request.session['g1'],
        'rand_goat2':request.session['g2']
    }
    return render(request, 'index.html', context)

def run_bet_custom(request):
    # need to update user with user from session.
    # this model is taking the names from the created custom match and pulling the player stats from the api, comparing them, generating the winner_name
    # and updating the Matchup object's "winner" attribute
    # and also updating the user's bank based on thier guess (won or lost)
    # currently this method redirects to a new page, i did that only becuase it was easier for testing
    goat1=request.POST['player1_goat']
    print(goat1)
    # player1=GOATdb.objects.get(full_name=goat1)
    # print(player1.id)
    goat2=request.POST['player2_goat']
    print(goat2)
    # player2=GOATdb.objects.get(full_name=goat2)
    # print(player2.id)
    user=User.objects.get(id=2)
    bank=user.bank
    bet=request.POST['bet_custom']
    # match=Matchup.objects.get(id=request.session['match_id'])
    querry1= goat1
    print(querry1)
    url = "https://nba-stats4.p.rapidapi.com/players/"
    querystring = {"page":"1","full_name":querry1,"per_page":"50"}
    headers = {
        'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
        'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response)
    resp_json=response.json()
    print(resp_json)
    player1_id=(resp_json[0]['id'])
    print(player1_id)
    url = "https://nba-stats4.p.rapidapi.com/per_game_career_regular_season/"
    headers = {
        'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
        'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
        }
    response = requests.request("GET", url+str(player1_id), headers=headers)
    print(response)
    resp_json_stats_p1=response.json()
    print(resp_json_stats_p1)
    player_name_p1=(resp_json[0]['full_name'])
    print(player_name_p1)
    querry2= goat2
    print(querry2)
    url = "https://nba-stats4.p.rapidapi.com/players/"
    querystring = {"page":"1","full_name":querry2,"per_page":"50"}
    headers = {
        'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
        'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response)
    resp_json=response.json()
    print(resp_json)
    player2_id=(resp_json[0]['id'])
    print(player2_id)
    new_match=Matchup.objects.create(
        goat1_id=player1_id,
        goat2_id=player2_id,
        user=user
    )
    url = "https://nba-stats4.p.rapidapi.com/per_game_career_regular_season/"
    headers = {
        'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
        'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
        }
    response = requests.request("GET", url+str(player2_id), headers=headers)
    print(response)
    resp_json_stats_p2=response.json()
    print(resp_json_stats_p2)
    player_name_p2=(resp_json[0]['full_name'])
    print(player_name_p2)
    list_p1=resp_json_stats_p1.values()
    print(list_p1)
    new_list_p1=[]
    for item in list_p1:
        if item!=None:
            new_list_p1.append(item)
        elif item==None:
            print(item)
            item=0
            print(item)
            new_list_p1.append(item)
        print(item)
    print(new_list_p1)
    new_list_p1.pop(0)
    new_list_p1.pop(0)
    new_list_p1.pop(0)
    print(new_list_p1)
    list_p2=resp_json_stats_p2.values()
    print(list_p2)
    new_list_p2=[]
    for item in list_p2:
        if item!=None:
            new_list_p2.append(item)
        elif item==None:
            print(item)
            item=0
            print(item)
            new_list_p2.append(item)
        print(item)
    print(new_list_p2)
    new_list_p2.pop(0)
    new_list_p2.pop(0)
    new_list_p2.pop(0)
    print(new_list_p2)
    print(len(new_list_p1))
    print(len(new_list_p2))
    p1_points=0
    p2_points=0
    for x in range(len(new_list_p1)):
            if new_list_p1[x] > new_list_p2[x]:
                p1_points+=1
            elif new_list_p1[x] < new_list_p2[x]:
                p2_points+=1
            # elif p1 == p2:
            #     continue
    print(p1_points)
    print(p2_points)
    new_match=Matchup.objects.create(
        goat1_id=player1_id,
        goat2_id=player2_id,
        user=user
    )
    if p1_points > p1_points:
        new_match.winner=player1_id
        winner_name=querry1
    else: 
        new_match.winner=player2_id
        new_match.save()
        winner_name=querry2
    print(new_match.winner)
    print(winner_name)
    request.session['winner'] = winner_name
    print(bank)
    print(bet)
    if request.POST['guess_custom']==winner_name:
        user.bank=int(bank)+int(bet)
        user.save()
        print(user.bank)
    else:
        user.bank=int(bank)-int(bet)
        user.save()
        print(user.bank)
    return redirect('/winner_page')


def winner_page(request):
    context={
        'winner': request.session['winner'],
        'user': User.objects.get(id=2)
    }
    return render(request, 'winner_page.html', context)

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

def run_bet_random(request):
    # need to update user with user from session.
    # This method also creates the matchup for the model class
    # this model is taking the names from the created custom match and pulling the player stats from the api, comparing them, generating the winner_name
    # and updating the Matchup object's "winner" attribute
    # and also updating the user's bank based on thier guess (won or lost)
    # currently this method redirects to a new page, i did that only becuase it was easier for testing
    user=User.objects.get(id=2)
    bank=user.bank
    random_bet=request.POST['bet_random']
    # match=Matchup.objects.get(id=request.session['match_id'])
    random_querry1= request.session['g1']
    print(random_querry1)
    url = "https://nba-stats4.p.rapidapi.com/players/"
    querystring = {"page":"1","full_name":random_querry1,"per_page":"50"}
    headers = {
        'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
        'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response)
    random_resp_json=response.json()
    print(random_resp_json)
    random_player1_id=(random_resp_json[0]['id'])
    print(random_player1_id)
    url = "https://nba-stats4.p.rapidapi.com/per_game_career_regular_season/"
    headers = {
        'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
        'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
        }
    response = requests.request("GET", url+str(random_player1_id), headers=headers)
    print(response)
    random_resp_json_stats_p1=response.json()
    print(random_resp_json_stats_p1)
    random_player_name_p1=(random_resp_json[0]['full_name'])
    print(random_player_name_p1)
    random_querry2= request.session['g2']
    print(random_querry2)
    url = "https://nba-stats4.p.rapidapi.com/players/"
    querystring = {"page":"1","full_name":random_querry2,"per_page":"50"}
    headers = {
        'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
        'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response)
    random_resp_json=response.json()
    print(random_resp_json)
    random_player2_id=(random_resp_json[0]['id'])
    print(random_player2_id)
    url = "https://nba-stats4.p.rapidapi.com/per_game_career_regular_season/"
    headers = {
        'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
        'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
        }
    response = requests.request("GET", url+str(random_player2_id), headers=headers)
    print(response)
    random_resp_json_stats_p2=response.json()
    print(random_resp_json_stats_p2)
    random_player_name_p2=(random_resp_json[0]['full_name'])
    print(random_player_name_p2)
    random_list_p1=random_resp_json_stats_p1.values()
    print(random_list_p1)
    random_new_list_p1=[]
    for item in random_list_p1:
        if item!=None:
            random_new_list_p1.append(item)
        elif item==None:
            print(item)
            item=0
            print(item)
            random_new_list_p1.append(item)
        print(item)
    print(random_new_list_p1)
    random_new_list_p1.pop(0)
    random_new_list_p1.pop(0)
    random_new_list_p1.pop(0)
    print(random_new_list_p1)
    random_list_p2=random_resp_json_stats_p2.values()
    print(random_list_p2)
    random_new_list_p2=[]
    for item in random_list_p2:
        if item!=None:
            random_new_list_p2.append(item)
        elif item==None:
            print(item)
            item=0
            print(item)
            random_new_list_p2.append(item)
        print(item)
    print(random_new_list_p2)
    random_new_list_p2.pop(0)
    random_new_list_p2.pop(0)
    random_new_list_p2.pop(0)
    print(random_new_list_p2)
    print(len(random_new_list_p1))
    print(len(random_new_list_p2))
    random_p1_points=0
    random_p2_points=0
    for x in range(len(random_new_list_p1)):
            if random_new_list_p1[x] > random_new_list_p2[x]:
                random_p1_points+=1
            elif random_new_list_p1[x] < random_new_list_p2[x]:
                random_p2_points+=1
            # elif p1 == p2:
            #     continue
    print(random_p1_points)
    print(random_p2_points)
    random_new_match=Matchup.objects.create(
        goat1_id=random_player1_id,
        goat2_id=random_player2_id,
        user=user
    )
    if random_p1_points > random_p1_points:
        random_new_match.winner=random_player1_id
        random_winner_name=random_querry1
    else: 
        random_new_match.winner=random_player2_id
        random_new_match.save()
        random_winner_name=random_querry2
    print(random_new_match.winner)
    print(random_winner_name)
    request.session['random_winner'] = random_winner_name
    print(bank)
    print(random_bet)
    if request.POST['guess_random']==random_winner_name:
        user.bank=int(bank)+int(random_bet)
        user.save()
        print(user.bank)
    else:
        user.bank=int(bank)-int(random_bet)
        user.save()
        print(user.bank)
    return redirect('/random_winner_page')

def random_winner_page(request):
    context={
        'random_winner': request.session['random_winner'],
        'user': User.objects.get(id=2)
    }
    return render(request, 'random_winner_page.html', context)

# def matchup_maker(request):
#     # this method is creating the custom match to include the names picked by the user, user must click submit.
#     # the names available are pre-loaded by admin into the GOATdb model class.  The admin can add more names too the model (to grow the list) but needs to use the api to retrieve the player_id
#     # for the player_id attribute
#     goat1=request.POST['player1_goat']
#     print(goat1)
#     player1=GOATdb.objects.get(full_name=goat1)
#     print(player1.id)
#     goat2=request.POST['player2_goat']
#     print(goat2)
#     player2=GOATdb.objects.get(full_name=goat2)
#     print(player2.id)
#     user=User.objects.get(id=2)
#     new_match=Matchup.objects.create(
#         goat1_id=player1.id,
#         goat2_id=player2.id,
#         user=user
#     )
#     request.session['goat1']= goat1
#     request.session['goat2']= goat2
#     request.session['match_id']=new_match.id
#     return redirect('/')

# def results(request):
#     querry=request.POST["search"]
#     url = "https://nba-stats4.p.rapidapi.com/players/"
#     querystring = {"page":"1","full_name":querry,"per_page":"50"}
#     headers = {
#         'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
#         'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
#         }
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     print(response)
#     resp_json=response.json()
#     print(resp_json)
#     player_id=(resp_json[0]['id'])
#     print(player_id)
#     url = "https://nba-stats4.p.rapidapi.com/per_game_career_regular_season/"
#     headers = {
#         'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
#         'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
#         }
#     response = requests.request("GET", url+str(player_id), headers=headers)
#     print(response)
#     resp_json_stats=response.json()
#     print(resp_json_stats)
#     player_name=(resp_json[0]['full_name'])
#     for key in resp_json_stats:
#         print(key, resp_json_stats[key])
#     context={
#         'player':player_name,
#         'stats':resp_json_stats
#     }
#     return render(request, 'results.html', context)

# def submit_custom(request):
#     user=User.objects.get(id=2)
#     print(user.first_name)
#     user.bet = request.POST['bet']
#     user.vote= request.POST['guess']
#     user.save()
#     print(user.bet)
#     print(user.vote)
#     print(user.bank)
#     return redirect('/')

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

# def player_search(request):
#     querry=request.POST["search"]
#     url = "https://nba-stats4.p.rapidapi.com/players/"
#     querystring = {"page":"1","full_name":querry,"per_page":"50"}
#     headers = {
#         'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
#         'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
#         }
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     print(response)
#     resp_json=response.json()
#     print(resp_json)
#     player_id=(resp_json[0]['id'])
#     print(player_id)
#     url = "https://nba-stats4.p.rapidapi.com/per_game_career_regular_season/"
#     headers = {
#         'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
#         'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
#         }
#     response = requests.request("GET", url+str(player_id), headers=headers)
#     print(response)
#     resp_json_stats=response.json()
#     print(resp_json_stats)
#     player_name=(resp_json[0]['full_name'])
#     for key in resp_json_stats:
#         print(key, resp_json_stats[key])
#     context={
#         'player':player_name,
#         'stats':resp_json_stats
#     }
#     request.session['current_goat_profile'] = resp_json
#     request.session['current_goat_stats'] = resp_json_stats
#     return render(request, 'create.html', context)

# def create(request):
#     user=User.objects.get(id=2)
#     players = GOAT.objects.filter(creator=user)
#     context={
#         'goats': players,
#     }
#     return render(request, 'create.html', context)

# def add_goat(request):
#     user=User.objects.get(id=2)
#     profile=request.session['current_goat_profile']
#     print(profile[0]['id'])
#     print(profile[0]['first_name'])
#     print(profile[0]['last_name'])
#     new_goat=GOAT.objects.create(
#         first_name=profile[0]['first_name'],
#         last_name=profile[0]['last_name'],
#         full_name=profile[0]['full_name'],
#         api_id=profile[0]['id'],
#         creator=user
#     )
#     return redirect('/create')

# def matchup_picker(request):
#     matches=Matchup.objects.all()
#     print(matches)
#     match=(random.choice(matches))
#     print(match)
#     p1=match.goat1_id
#     p2=match.goat2_id
#     player1=GOAT.objects.get(id=p1).full_name
#     player2=GOAT.objects.get(id=p2).full_name
#     request.session['goat1']=player1
#     request.session['goat2']=player2
#     return redirect('/')

# def stats_comp(request):
#     goat_list=GOATdb.objects.all()
#     player1=(random.choice(goat_list))
#     print(player1)
#     querry= player1.full_name
#     print(querry)
#     url = "https://nba-stats4.p.rapidapi.com/players/"
#     querystring = {"page":"1","full_name":querry,"per_page":"50"}

#     headers = {
#         'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
#         'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
#         }
    # response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response)
    # resp_json=response.json()
    # print(resp_json)
    # player_id=(resp_json[0]['id'])
    # print(player_id)
    # url = "https://nba-stats4.p.rapidapi.com/per_game_career_regular_season/"
    # headers = {
    #     'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
    #     'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
    #     }
    # response = requests.request("GET", url+str(player_id), headers=headers)
    # print(response)
    # resp_json_stats_p1=response.json()
    # print(resp_json_stats_p1)
    # player_name_p1=(resp_json[0]['full_name'])
    # print(player_name_p1)
    # player2=(random.choice(goat_list))
    # print(player2)
    # querry= player2.full_name
    # print(querry)
    # url = "https://nba-stats4.p.rapidapi.com/players/"
    # querystring = {"page":"1","full_name":querry,"per_page":"50"}
    # headers = {
    #     'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
    #     'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
    #     }
    # response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response)
    # resp_json=response.json()
    # print(resp_json)
    # player_id=(resp_json[0]['id'])
    # print(player_id)
    # url = "https://nba-stats4.p.rapidapi.com/per_game_career_regular_season/"
    # headers = {
    #     'x-rapidapi-host': "nba-stats4.p.rapidapi.com",
    #     'x-rapidapi-key': "4622709193msh2b7cd6a6ebba26bp101347jsn0d99950ce664"
    #     }
    # response = requests.request("GET", url+str(player_id), headers=headers)
    # print(response)
    # resp_json_stats_p2=response.json()
    # print(resp_json_stats_p2)
    # player_name_p2=(resp_json[0]['full_name'])
    # print(player_name_p2)
    # list_p1=resp_json_stats_p1.values()
    # print(list_p1)
    # new_list_p1=[]
    # for item in list_p1:
    #     if item!=None:
    #         new_list_p1.append(item)
    #     elif item==None:
    #         print(item)
    #         item=0
    #         print(item)
    #         new_list_p1.append(item)
    #     print(item)
    # print(new_list_p1)
    # new_list_p1.pop(0)
    # new_list_p1.pop(0)
    # new_list_p1.pop(0)
    # print(new_list_p1)
    # list_p2=resp_json_stats_p2.values()
    # print(list_p2)
    # new_list_p2=[]
    # for item in list_p2:
    #     if item!=None:
    #         new_list_p2.append(item)
    #     elif item==None:
    #         print(item)
    #         item=0
    #         print(item)
    #         new_list_p2.append(item)
    #     print(item)
    # print(new_list_p2)
    # new_list_p2.pop(0)
    # new_list_p2.pop(0)
    # new_list_p2.pop(0)
    # print(new_list_p2)
    # print(len(new_list_p1))
    # print(len(new_list_p2))
    # p1_points=0
    # p2_points=0
    # for x in range(len(new_list_p1)):
    #         if new_list_p1[x] > new_list_p2[x]:
    #             p1_points+=1
    #         elif new_list_p1[x] < new_list_p2[x]:
    #             p2_points+=1
    #         # elif p1 == p2:
    #         #     continue
    # print(p1_points)
    # print(p2_points)
    # return redirect('/')