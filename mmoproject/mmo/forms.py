from django import forms

class SearchUserForm(forms.Form):
    #Search bar to search a player account
    account_name = forms.CharField(label='Search Account Name', max_length=100)