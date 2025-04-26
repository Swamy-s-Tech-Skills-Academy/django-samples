from django.urls import path
from . import views

app_name = 'challenges'

urlpatterns = [
    path('', views.challenges_index_view, name='index'),
    path('<str:month>', views.challenge_detail_view, name='detail'),
]