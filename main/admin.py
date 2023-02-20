from django.contrib import admin
from .models import Sites, SiteComment, SiteProfile, UserSite, UserSiteProfile

admin.site.register(Sites)
admin.site.register(SiteComment)
admin.site.register(SiteProfile)
admin.site.register(UserSite)
admin.site.register(UserSiteProfile)