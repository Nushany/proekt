from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import SignUpForm

def index(request):
    return render(request, 'shopapp/index.html')

def biology(request):
    return render(request, 'shopapp/biology.html')

def chemistry(request):
    return render(request, 'shopapp/chemistry.html')

def list(request):
    return render(request, 'shopapp/list.html')

def profile(request):
    return render(request, 'shopapp/profile.html')

def info(request):
    return render(request, 'shopapp/info.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'shopapp/signup.html', {'form': form})