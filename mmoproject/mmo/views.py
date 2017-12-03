from operator import concat
from django.shortcuts import render
from .models import PlayerAccount
from .forms import SearchUserForm
from django.http import HttpResponseRedirect
# Create your views here.


def home(request):
    if request.method == 'POST':
        search_form = SearchUserForm(request.POST)
        if search_form.is_valid():
            #Get username to search for from form
            acc_name = search_form.cleaned_data['account_name']

            #redirect to the user's page if the name matches an account in the database;
            #redirect to search results otherwise
            if(PlayerAccount.objects.filter(uName=acc_name)):
                return HttpResponseRedirect('/mmo/user/{}'.format(acc_name))
            else:
                return HttpResponseRedirect('/mmo/usearch_result/{}'.format(acc_name))
    else:
        search_form = SearchUserForm()

    return render(request, 'mmo/home.html', {'search_form': search_form})

def user(request, name):
    account = PlayerAccount.objects.filter(uName=name).get()
    return render(request, 'mmo/user.html', {'account': account})


def usearch_result(request, target):
    results = PlayerAccount.objects.filter(uName__contains=target)
    return render(request, 'mmo/usearch_result.html', {'results':results})
