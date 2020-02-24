from django.db import models

class Review(models.Model):
    review = models.IntegerField()
    body = models.TextField()
    author = models.CharField(max_length=255)
    date = models.DateField()
    cover = models.ImageField()
    album = models.CharField(max_length=25)
    artist = models.CharField(max_length=255)

    def __str__(self):
        return self.album + "-" + self.artist