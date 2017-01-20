from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):

    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
   
    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1', 'password2' )

    #def save(self, commit=True):
    #    user = super(UserCreationForm, self).save(commit=False)
    #    user.email = self.cleaned_data['email']
    #    user.first_name = self.cleaned_data['first_name']
    #    user.last_name = self.cleaned_data['last_name']
    #    user.nickname= self.cleaned_data['nickname']

    #    if commit:
    #        user.save()
 
    #    return user
