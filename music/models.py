from django.db import models
from django.urls import reverse

class Album(models.Model):
    artist = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    genre = models.CharField(max_length=256)
    logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + " - " + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    ext = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    is_favourite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.album.pk})

    def __str__(self):
        return self.title