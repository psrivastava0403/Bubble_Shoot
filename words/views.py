from django.shortcuts import render
from django.http import JsonResponse
from .models import AlphabetEntry
import random

def game_view(request):
    return render(request, 'game.html')

def get_entries(request):
    entries = AlphabetEntry.objects.all()
    letter_map = {}
    for entry in entries:
        letter = entry.first_letter()
        if letter not in letter_map:
            letter_map[letter] = []
        letter_map[letter].append({
            'word': entry.word,
            'image': entry.image.url
        })
    return JsonResponse(letter_map)
