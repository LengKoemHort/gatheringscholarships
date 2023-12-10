from django.http import HttpResponse
from django.shortcuts import render
from social_django.models import UserSocialAuth
from allauth.socialaccount.models import SocialAccount

def home(request):
    return render(request, 'account/base.html')

def login_view(request):
    return render(request, 'account/login.html')

def international_view(request):
    return render(request, 'account/international.html')

def local_view(request):
    return render(request, 'account/local.html')

def login_view(request):
    return render(request, 'account/login.html')

def profile(request):
    try:
        social_account = SocialAccount.objects.get(user=request.user)
        google_profile = social_account.extra_data
    except SocialAccount.DoesNotExist:
        google_profile = None   
    return render(request, 'account/profile.html', {'google_profile': google_profile})

