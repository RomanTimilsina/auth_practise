from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return 'success'
    else:
        initial_data = {'username': '', 'password1': '', 'password2': ''}
        form = UserCreationForm(initial = initial_data)
    return render(request, 'auth/register.html', {'form' : form})

def login_view(request):
    pass

def dashboard_view(request):
    pass

def logout_view(request):
    pass