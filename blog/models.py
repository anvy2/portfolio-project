from django.db import models

class Blog(models.Model):
    Title = models.CharField(max_length = 150)
    Date = models.DateTimeField()
    Description = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.Title

    def summary(self):
        return self.Description[:100]

    def time(self):
        return self.Date.strftime('%b %e %Y')
