from django import forms
from .models import User


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    website = forms.URLField()
    class Meta:
        model = User
        fields = ('username','password','firstname','lastname','email','website',)


    
class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email', 'website',)

