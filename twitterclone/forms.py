# from django import forms
# from django.contrib.auth.forms import UserCreationForm

# from twitteruser.models import CustomUser


# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = [
#             'display_name',
#             'username',
#             'email'
#         ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
