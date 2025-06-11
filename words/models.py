from django.db import models

class AlphabetEntry(models.Model):
    word = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='alphabet_images/')

    def first_letter(self):
        return self.word[0].upper()

    def __str__(self):
        return f"{self.word.capitalize()} ({self.first_letter()})"
