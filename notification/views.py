from django.shortcuts import render, reverse, HttpResponseRedirect
from notification.models import Notification
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification
from twitteruser.models import TwitterUser
from tweet.models import Tweet


def notification_view(request):
    try:
        notifications = list(
            Notification.objects.filter(recipient=request.user))
        Notification.objects.filter(recipient=request.user).delete()
        users = TwitterUser.objects.all()
        tweets = Tweet.objects.all()
    except Exception:
        return HttpResponseRedirect(reverse('home'))
    
    return render(request, 'notifications.html', {
        'notifications': notifications,
        'users': users,
        'tweets': tweets
    })
