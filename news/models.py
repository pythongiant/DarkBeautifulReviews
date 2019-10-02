from django.db import models

# Create your models here.
class News(models.Model):
    date = models.DateTimeField()
    author = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField()
    def __str__(self):
        return self.name+"("+str(self.date)+")"