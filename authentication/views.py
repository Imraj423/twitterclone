from django.contrib.auth import logout
from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
# from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from django.contrib.auth import logout as auth_logout
from django.views.generic import RedirectView
from django.conf import settings
# def logoutUser(request):
#     logout(request)
#     return HttpResponseRedirect('/login/')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)


class Login_View(View):
    form_class = LoginForm
    initial = {'key': 'value'}
    template_name = 'generic_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            form = LoginForm()

        return render(request, self.template_name, {'form': form})


# def login_view(request):
#     html = 'generic_form.html'
#     if request.method == 'POST':
#         form = LoginForm(request.POST)

#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(
#                 username=data['username'], password=data['password'])
#             if user is not None:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('home'))
#     else:
#         form = LoginForm()

#     return render(request, html, {'form': form})


# def signup(request):
#     html = 'generic_form.html'

#     if request.method == 'POST':
#         form = SignUpForm(request.POST)

#         if form.is_valid():
#             data = form.cleaned_data
#             user = TwitterUser.objects.create_user(
#                 data['username'],
#                 data['password'], display_name=data['display_name']
#             )
#             login(request, user)
#             return HttpResponseRedirect(reverse('login'))
#     else:
#         form = SignUpForm()
#     return render(request, html, {'form': form})


class SignUp_View(View):
    form_class = SignUpForm
    initial = {'key': 'value'}
    template_name = 'generic_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = TwitterUser.objects.create_user(
                data['username'],
                data['password'], display_name=data['display_name']
            )
            login(request, user)
            return HttpResponseRedirect('/login')
        else:
            form = SignUpForm()
        return render(request, self.template_name, {'form': form})
