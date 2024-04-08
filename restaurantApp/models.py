from django.db import models

class Restaurant(models.Model):
    nombre = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.nombre