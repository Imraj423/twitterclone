from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('notification.urls')),
    path('', include('authentication.urls')),
    path('', include('tweet.urls')),
    path('', include('twitteruser.urls')),

    
]
