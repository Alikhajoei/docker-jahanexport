from .models import Footer, SocialMediaLink
from django.db.models.signals import pre_save
from django.dispatch import receiver

@receiver(pre_save, sender=Footer)
def deactivate_previous_footer(sender, instance, *args, **kwargs):
    if instance.activate:
        Footer.objects.filter(activate=True).update(activate=False)
        
        
@receiver(pre_save, sender=SocialMediaLink)
def deactivate_previous_social_media_link(sender, instance, *args, **kwargs):
    if instance.activate:
        SocialMediaLink.objects.filter(activate=True).update(activate=False)