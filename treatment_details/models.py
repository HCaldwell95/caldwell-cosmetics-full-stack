from django.db import models

# Create your models here.

class Treatment(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='treatments/')
    description = models.TextField()

    def __str__(self):
        return self.name