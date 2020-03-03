from django.shortcuts import render, HttpResponseRedirect, reverse
from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
# from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notification.models import Notification


# def home(request):
#     html = 'index.html'
#     return render(request, html, {
#         'user_type': str(type(TwitterUser.objects.get(id=request.user.id)))
#     })

@login_required(login_url="/login/")
def home(request):
    following = list(TwitterUser.objects.get(
        username=request.user).following.all())
    following.append(request.user)
    print(following)
    item = Tweet.objects.filter(twitter_user__in=following)
    return render(request, 'index.html', {'data': item})


@login_required(login_url="/login/")
def profile_view(request, id):
    html = "profile.html"
    tweet_views = Tweet.objects.filter(twitter_user=id)
    tweet_count = tweet_views.count()
    user = TwitterUser.objects.get(id=request.user.id)
    tweets = Tweet.objects.filter(twitter_user=user)
    following = user.following
    following_count = following.count()
    print(following, following_count, tweets, user)
    return render(request,
                  html,
                  {
                        'user_type': str(type(TwitterUser.objects.get(
                            id=request.user.id))),
                        'id': id,
                        'tweet_views': tweet_views,
                        'tweet_count': tweet_count,
                        'tweets': tweets,
                        'following_count': following_count,
                        'following': following
                  }
                  )
