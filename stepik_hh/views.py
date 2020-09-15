from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", 'first_name', 'last_name')


class MySignupView(CreateView):
    form_class = MyUserCreationForm
    success_url = 'ylogin'
    template_name = 'signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
