from django.contrib import admin
from .models import Footer,SiteImage,SiteVideo,SocialMediaLink
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(Footer)
admin.site.register(SocialMediaLink)
admin.site.register(SiteImage)
admin.site.register(SiteVideo)
admin.site.unregister(Group)