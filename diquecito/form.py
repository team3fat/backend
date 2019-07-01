from django import forms
from diquecito.models import UserProfileInfo
from django.contrib.auth.models import Userclass UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')
