from django.db import models

class Blog(models.Model):
    Title = models.CharField(max_length = 150)
    Publication_date = models.DateTimeField()
    Description = models.TextField()
    image = models.ImageField(upload_to = 'images/')
