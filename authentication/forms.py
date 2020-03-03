from django import forms
# from django.contrib.auth.forms import UserCreationForm

# from twitteruser.models import TwitterUser


# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = TwitterUser
#         fields = [
#             'display_name',
#             'username'

#         ]

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    display_name = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
