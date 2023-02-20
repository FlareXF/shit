from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image

class Sites(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=600)

    values = models.JSONField(default=dict)
    reports = models.JSONField(default=dict)

    def __str__(self):
        return self.name


class SiteProfile(models.Model):
    site = models.OneToOneField(Sites, on_delete=models.CASCADE)
    image = models.ImageField(default="site_default.png", upload_to="site_pics")

    def __str__(self):
        return self.site.url

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.image.path)
        if image.height > 300 or image.width > 300:
            out_size = (300,300)
            image.thumbnail(out_size)
            image.save(self.image.path)


class UserSite(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=600)
    values = models.JSONField(default=dict)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner.username}-{self.name}"
    
    def get_absolute_url(self):
        return reverse("user-site", kwargs={"pk": self.pk})

class UserSiteProfile(models.Model):
    site = models.OneToOneField(UserSite, on_delete=models.CASCADE)
    image = models.ImageField(default="site_default.png", upload_to="user_site_pics")

    def __str__(self):
        return self.site.url

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.image.path)
        if image.height > 300 or image.width > 300:
            out_size = (300,300)
            image.thumbnail(out_size)
            image.save(self.image.path)



class SiteComment(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    site = models.ForeignKey(Sites, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.user.username} - {self.date}"