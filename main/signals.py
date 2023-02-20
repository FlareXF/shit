from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SiteProfile, Sites, UserSite, UserSiteProfile


@receiver(post_save, sender=Sites)
def create_profile(sender, instance, created, **kwargs):
	if created:
		SiteProfile.objects.create(site=instance)

@receiver(post_save, sender=Sites)
def save_profile(sender, instance, **kwargs):
	instance.siteprofile.save()


@receiver(post_save, sender=UserSite)
def create_profile(sender, instance, created, **kwargs):
	if created:
		UserSiteProfile.objects.create(site=instance)

@receiver(post_save, sender=UserSite)
def save_profile(sender, instance, **kwargs):
	instance.usersiteprofile.save()