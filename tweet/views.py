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
            tweet = Tweet.objects.create(
                body=data['body'],
                twitter_user=request.user
            )
            for word in data["body"].split(" "):
                if word.startswith("@"):
                    username = word[1:]
                    users = TwitterUser.objects.filter(username=username)
                    if users.exists():
                        Notification.objects.create(
                            recipient=users.first(),
                            tweet=tweet
                        )
        return HttpResponseRedirect(reverse("home"))
    form = addPost()

    return render(request, html, {'form': form})


def tweet_detail_view(request, tweet_id):
    tweet = None
    users = None

    try:
        users = TwitterUser.objects.all()
        tweet = Tweet.objects.get(id=tweet_id)
    except Exception:
        return HttpResponseRedirect(reverse('home'))

    return render(request, 'detail.html', {
        'tweet': tweet,
        'users': users
    })
