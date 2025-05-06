from django.db import models

class Slides(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='slides/')
