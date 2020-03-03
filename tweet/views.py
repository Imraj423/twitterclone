from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Tweet
from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import addPost
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from notification.models import Notification

@login_required(login_url="/login/")
def post_add(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = addPost(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                body=data['body'],
                twitter_user=request.user
            )
            for word in data["body"].split(" "):
                if word.startswith("@"):
                    username = word[1:]
                    users = TwitterUser.objects.filter(username=username)
                    if users.exists():
                        Notification.objects.create(
                            follow_target=users.first(),
                            body=data['body']
                        )
        return HttpResponseRedirect(reverse("home"))
    form = addPost()

    return render(request, html, {'form': form})


def following_view(request, id):
    follow_target = TwitterUser.objects.get(id=id)
    current_user = request.user
    current_user.following.add(follow_target)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
