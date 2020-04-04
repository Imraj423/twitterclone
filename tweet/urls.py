from django.urls import path
from . import views


urlpatterns = [
    path('addpost/', views.post_add, name='write_tweet'),
    path('tweet/<int:tweet_id>', views.tweet_detail_view, name='tview')

]

