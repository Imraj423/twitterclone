from .views import Post_Add
from django.urls import path
from . import views


# urlpatterns = [
    # path('addpost/', views.post_add, name='write_tweet'),
    
# ]


urlpatterns = [
    path('addpost/', Post_Add.as_view()),
    path('follow/<int:id>/', views.following_view, name='follow')
    ]
    