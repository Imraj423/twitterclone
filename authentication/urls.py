from django.urls import path
from . import views
from .views import Login_View, SignUp_View, LogoutView
# , LogoutView

urlpatterns = [
    path('signup/', SignUp_View.as_view(), name='signup'),
    path('login/', Login_View.as_view(), name='login'),
    # path('logout/', views.logoutUser, name='logout'),
    path('logout/', LogoutView.as_view())
    ]
