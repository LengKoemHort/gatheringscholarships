from django.urls import re_path, path
from ScholarshipApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^international$', views.internationalApi),
    re_path(r'^international/([0-9]+)$', views.internationalApi),

    re_path(r'^local$', views.localApi),
    re_path(r'^local/([0-9]+)$', views.localApi),
]
