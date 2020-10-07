from django.contrib.auth.views import LogoutView
from django.urls import path

from app_authentication.views import MyLoginView, MySignupView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', MySignupView.as_view(), name='signup'),
]
