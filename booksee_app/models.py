from django.db import models

class Genre(models.Model):
    genre_name = models.CharField(max_length=264, unique=True)
    def __str__(self):
        return self.genre_name

class Award(models.Model):
    award_name = models.CharField(max_length=264, unique=True)
    def __str__(self):
        return self.award_name

class Language(models.Model):
    language_name = models.CharField(max_length=264, unique=True)
    def __str__(self):
        return self.language_name
