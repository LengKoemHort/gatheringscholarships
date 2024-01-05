from django.http import HttpResponse
from django.shortcuts import render, redirect
from social_django.models import UserSocialAuth
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout

def home(request):
    return render(request, 'account/base.html')
def international_view(request):
    return render(request, 'account/itn.html')
def local_view(request):
    return render(request, 'account/loc.html')
def aboutus_view(request):
    return render(request, 'account/aboutus.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to 'profile' view after successful login
        else:
            return render(request, 'account/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'account/login.html')

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Ensure the message is added only once
            messages.success(request, 'You have successfully registered! Please log in.')
            return redirect('account_login')  # Replace 'account_login' with your login URL name
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('home') 

def profile(request):
    try:
        social_account = SocialAccount.objects.get(user=request.user)
        google_profile = social_account.extra_data
    except SocialAccount.DoesNotExist:
        google_profile = None   
    return render(request, 'account/profile.html', {'google_profile': google_profile})

