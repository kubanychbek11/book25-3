from django.db import models

class BookParser(models.Model):
    title_url = models.CharField(max_length=100)
    title_text = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    #info = models.TextField()

    def __str__(self):
        return self.title_text