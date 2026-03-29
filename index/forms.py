from django import forms


class UserForm(forms.Form):
    hashtag = forms.CharField(max_length=100)
    num = forms.CharField(max_length=100)
