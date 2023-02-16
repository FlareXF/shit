from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Sites(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=600)

    values = models.JSONField()
    #reports = models.JSONField()

    def __str__(self):
        return self.name


class UserSite(Sites):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner - self.name}"
    
    def get_absolute_url(self):
        return reverse("user-site", kwargs={"pk": self.pk})


class SiteComment(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    site = models.ForeignKey(Sites, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    content = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.user.username} - {self.date}"