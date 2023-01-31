from django.db import models

class Sites(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=600)

    values = models.JSONField()

    def __str__(self):
        return self.name