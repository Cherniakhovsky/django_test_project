from django import forms
from django.contrib.auth.models import User
#from balance.models import Client,Cost


# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     #your_name = forms.CharField(label='Your name', max_length=100)
#     class Meta:
#         model = Client
#         fields = ('passport_number',)
#
#
#
# class CostForm(forms.ModelForm):
#     #password = forms.CharField(widget=forms.PasswordInput())
#     #your_name = forms.CharField(label='Your name', max_length=100)
#     class Meta:
#         model = Cost
#         fields = ('username','date', 'cost_description', 'cost', 'balance',)
