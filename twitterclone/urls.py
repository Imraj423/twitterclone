from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Home_View


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home_View.as_view(), name='home'),
    path('profile/<int:id>/', views.profile_view, name='profile'),
    path('', include('notification.urls')),
    path('', include('authentication.urls')),
    path('', include('tweet.urls')),
    # path('', include('twitteruser.urls')),
    
]
