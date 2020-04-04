import re
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notification.models import Notification


@login_required(login_url="/login/")
def home(request):
    following = list(TwitterUser.objects.get(
        username=request.user).following.all())
    # following.append(request.user)
    item = Tweet.objects.filter(twitter_user__in=following)
    notifications = Notification.objects.filter(recipient=request.user)
    tweets = Tweet.objects.all()
    tuser = TwitterUser.objects.all()
    
    return render(request, 'index.html', {'item': item, 'following': following,
                                          'notifications': notifications,
                                          'tweets': tweets, 'tuser': tuser,
                                          })


def notify(tweet):
    mention_pattern = r'([@#][\w_-]+)'
    tag = re.match(mention_pattern, tweet.body)
    if tag:
        try:
            tagged_user = TwitterUser.objects.get(username=tag.group()[1:])
            Notification.objects.create(
                recipient=tagged_user,
                tweet=tweet
            )
        except Exception:
            pass


# def profile_view(request, id):
#     html = "profile.html"
#     tweet_views = Tweet.objects.filter(twitter_user=id)
#     tweet_count = tweet_views.count()
#     user = TwitterUser.objects.get(id=request.user.id)
#     tweets = Tweet.objects.filter(twitter_user=user)
#     following = user.following
#     following_count = following.count()
#     print(following, following_count, tweets, user)
#     return render(request,
#                   html,
#                   {
#                         'user_type': str(type(TwitterUser.objects.get(
#                             id=request.user.id))),
#                         'id': id,
#                         'tweet_views': tweet_views,
#                         'tweet_count': tweet_count,
#                         'tweets': tweets,
#                         'following_count': following_count,
#                         'following': following
#                   }
#                   )
