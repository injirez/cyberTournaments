from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('byDate', views.byDateDota),
    path('byReward', views.byRewardDota)
]
