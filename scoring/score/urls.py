from . import views

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path('', views.list_scores, name='score.list'),
    path('new', views.new_score, name='score.create'),
]
