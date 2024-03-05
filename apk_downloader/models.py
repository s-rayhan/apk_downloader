from django.db import models

class Apk(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='apks/')
    downloads = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
