from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    path('', views.home, name='home'),
    path('international/', views.international_view, name='international'),
    path('local/', views.local_view, name='local'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('allauth.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('aboutus/', views.aboutus_view, name='aboutus'),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('signup/', views.sign_up, name='signup'),
    path('', include('ScholarshipApp.urls')),

]
