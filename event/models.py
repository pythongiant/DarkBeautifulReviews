from django.db import models

# Create your models here.
class event(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    link = models.URLField()
    def __str__(self):
        return self.name+"("+str(self.date)+")"
