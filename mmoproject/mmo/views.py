from operator import concat
from django.shortcuts import render
from .models import PlayerAccount
from .forms import SearchUserForm
from django.http import HttpResponseRedirect
from . import sqlHandler as sql
# Create your views here.


def home(request):
    if request.method == 'POST':
        search_form = SearchUserForm(request.POST)
        if search_form.is_valid():
            #Get username to search for from form
            acc_name = search_form.cleaned_data['account_name']

            #redirect to the user's page if the name matches an account in the database;
            #redirect to search results otherwise
            if sql.findAccount(acc_name):
                return HttpResponseRedirect('/mmo/user/{}'.format(acc_name))
            else:
                return HttpResponseRedirect('/mmo/usearch_result/{}'.format(acc_name))
    else:
        search_form = SearchUserForm()

    return render(request, 'mmo/home.html', context={'search_form': search_form})

def user(request, name):
    account = sql.findAccount(name)
    return render(request, 'mmo/user.html', context={'account': account})

def usearch_result(request, target):
    results = sql.findAccountLike(target)

    return render(request, 'mmo/usearch_result.html', context={'results': results, 'target':target})

def character(request, charName):

    return render(request, 'mmo/character.html', context={})