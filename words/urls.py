from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_view, name='game'),
    path('api/entries/', views.get_entries, name='get_entries'),
]