from django.db import models

class Object(models.Model):
    title = models.CharField(max_length=200)
    descripshon = models.TextField()
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField()
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title