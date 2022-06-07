# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('running/', views.running),
    path('addweight/', views.addweight),
    path('addrun/', views.addrun),
    path('logweight/', views.logweight),
]