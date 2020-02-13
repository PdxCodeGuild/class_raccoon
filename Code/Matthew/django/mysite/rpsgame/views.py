from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import RPSGame
import random

# Create your views here.
def index(request):
    games = RPSGame.objects.order_by("-timestamp")
    result = request.GET.get("result", "")
    playername = request.GET.get("playername", "")
    winrecord = RPSGame.objects.filter(humanwin=True).count()
    loserecord = RPSGame.objects.filter(humanwin=False).count()
    context = {
        "games":games,
        "result":result,
        "playername":playername,
        "winrecord":winrecord,
        "loserecord":loserecord,
        }
    return render(request,"rpsgame/index.html", context)

def countwins():
    games = RPSGame.objects.all()
    playerdict = {}
    for game in games:
        if game.playername in playerdict:
            if game.humanwin:
                playerdict[game.playername]+=1
            else:
                playerdict[game.playername]-=1
        else:
            if game.humanwin:
                playerdict[game.playername]=1
            else:
                playerdict[game.playername]=-1
    scores = list(playerdict.items())
    scores.sort(key=lambda x:x[1], reverse=True)
    return scores

def play(request):
    playername = request.POST['playername']
    playerchoice = request.POST['playerchoice']
    moves = ['Rock','Paper','Scissors']
    compchoice = random.choice(moves)
    result = None
    if playerchoice == compchoice:
        return HttpResponseRedirect(reverse("rpsgame:index")+"?result=tie&playername="+playername)
    elif playerchoice == 'Rock':
        if compchoice == 'Paper':
            result = 'lose'
        else:
            result = 'win'
    elif playerchoice == 'Paper':
        if compchoice == 'Scissors':
            result = 'lose'
        else:
            result = 'win'
    else:
        if compchoice == 'Rock':
            result = 'lose'
        else:
            result = 'win'
    game = RPSGame(playername=playername, playerchoice=playerchoice, compchoice=compchoice, timestamp=timezone.now(), humanwin=(result=='win'))
    game.save()
    return HttpResponseRedirect(reverse("rpsgame:index")+"?result="+result+"&playername="+playername)

def score(request):
    scores = countwins()
    context = {
        "scores":scores
    }
    return render(request, "rpsgame/leaderboard.html", context)