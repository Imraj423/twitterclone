from django.shortcuts import render, reverse, HttpResponseRedirect
# from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from twitteruser.models import TwitterUser


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def login_view(request):
    html = 'generic_form.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginForm()

    return render(request, html, {'form': form})


def signup(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = TwitterUser.objects.create_user(
                data['username'],
                data['password'], display_name=data['display_name']
            )
            login(request, user)
            return HttpResponseRedirect(reverse('login'))
    else:
        form = SignUpForm()
    return render(request, html, {'form': form})
