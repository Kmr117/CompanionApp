from django.shortcuts import render
from .forms import SearchUserForm
from django.http import HttpResponseRedirect
from . import sqlHandler as sql
from django.views import View
# Create your views here.


def home(request):
    return render(request, 'mmo/home.html')

def addUser(request):
    if request.method == 'POST':
        username = request.POST["addUserName"]
        email = request.POST["addUserEmail"]
        password = request.POST["addUserPassword"]
        sql.CreateAccount(username=username,email=email,password=password)
    return render(request,'mmo/user.html')

def usearch_result(request, target):
    results = sql.findAccountLike(target)

    return render(request, 'mmo/usearch_result.html', context={'results': results, 'target': target})

def characterDetail(request, detailTarget):
    character = sql.findCharacter(detailTarget)
    items = sql.findItems(detailTarget)
    return render(request, 'mmo/character_detail.html', context={'character': character, 'inventory':items})

def playerDetail(request, name):
    user = sql.findAccount(name)
    characters = sql.findAllCharacter(name)
    friends = sql.getFriendList(name)
    return render(request, 'mmo/player_detail.html', context={'player': user, 'characters': characters, 'friends': friends})


class characterView(View):
    def get(self, request, charName=''):
        if charName == '':
            return render(request, 'mmo/character.html', context={'character': None, 'inventory': None})

    def post(self, request):
        charName = request.POST['name']
        if charName:
            character = sql.findCharacter(charName)
            if character is not None:
                return HttpResponseRedirect('/mmo/character/detail/{}'.format(charName))



class userView(View):
    def get(self, request, name=''):
        if name == '':
            return render(request, 'mmo/user.html')

    def post(self, request):

        if 'user' in request.POST:
            # redirect to the user's page if the name matches an account in the database;
            # redirect to search results otherwise
            name = request.POST['user']
            player = sql.findAccount(name)
            if player is not None:
                return HttpResponseRedirect('/mmo/user/detail/{}'.format(player.userName))
            else:
                return HttpResponseRedirect('/mmo/usearch_result/{}'.format(name))
        else:
            newName = request.POST['addUserName']
            newEmail = request.POST['addUserEmail']
            newPassword = request.POST['addUserPassword']
            sql.CreateAccount(newName, newEmail, newPassword)
            return render(request, 'mmo/user.html')