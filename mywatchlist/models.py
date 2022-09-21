from django.db import models

# Create your models here.
class WatchlistMovie(models.Model):
    movie_title = models.CharField(max_length=255)
    release_date = models.TextField(default='')
    watched = models.TextField(default='')
    movie_rating = models.IntegerField(default=0)
    movie_review = models.TextField(default='')
