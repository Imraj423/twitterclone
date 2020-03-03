from django.urls import path
from . import views


urlpatterns = [
    path('addpost/', views.post_add, name='write_tweet'),
    path('follow/<int:id>/', views.following_view, name='follow'),
]
