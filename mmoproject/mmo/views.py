from operator import concat
from django.shortcuts import render
from .models import PlayerAccount
from .forms import SearchUserForm
from django.http import HttpResponseRedirect
from . import sqlHandler as sql
# Create your views here.


def home(request):
     #if request.method == 'POST':
      #   search_form = SearchUserForm(request.POST)
       #  if search_form.is_valid():
        #     Get username to search for from form
         #    acc_name = search_form.cleaned_data['account_name']
    #
    #         #redirect to the user's page if the name matches an account in the database;
    #         #redirect to search results otherwise
    #         if sql.findAccount(acc_name):
    #             return HttpResponseRedirect('/mmo/user/{}'.format(acc_name))
    #         else:
    #             return HttpResponseRedirect('/mmo/usearch_result/{}'.format(acc_name))
    # else:
    #     search_form = SearchUserForm()

    return render(request, 'mmo/home.html')

def user(request):
    print (request)
    if request.method == 'POST':
        name = request.POST["user"]
        if name:
        #search_form = SearchUserForm(request.POST["user"])
        #if search_form.is_valid():
            # Get username to search for from form
            acc_name = name#search_form.cleaned_data['account_name']

            # redirect to the user's page if the name matches an account in the database;#
            # redirect to search results otherwise
            player = sql.findAccount(acc_name)
            if player is not None:
                return render(request,'mmo/user.html',context = {"account":player})

            #return HttpResponseRedirect('/mmo/user/{}'.format(acc_name))
            else:
                return HttpResponseRedirect('/mmo/usearch_result/{}'.format(acc_name))
    else:
        return render(request, 'mmo/user.html', context={'account': None})

    #else:
     #   print("hello")
      #  search_form = SearchUserForm()
       # if not name:
        #    account = sql.findAccount(name)
         #   return render(request, 'mmo/user.html', context={'account': account, 'search_form': search_form})

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

def character(request):
    if request.method == 'POST':
        print("hello")
    #char = sql.findCharacter(charName)
    return render(request, 'mmo/character.html',) #context={'character': char, 'target': charName})

def character1(request):
    char = None
    if request.method =='POST':
        print("hello")
        charName = request.POST["name"]
        char = sql.findCharacter(charName)
        return render(request,'mmo/character.html' ,context = {"character":char})

    return render(request,'mmo/character.html',)

def character2(request):
    items = None
    if request.method =='POST':
        name = request.POST["inventory"]
        items = sql.findItems(name)
        print("this is ")
        print(items)
        return render(request, 'mmo/character.html', context={"inventory":items})

    #return render(request,'mmo/character.html',)

