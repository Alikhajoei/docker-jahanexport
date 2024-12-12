from .models import HomeController,FestivalSale
from django.db.models.signals import pre_save
from django.dispatch import receiver



@receiver(pre_save,sender = HomeController)
def deactive_home_previous(sender,instance,*args, **kwargs):
    if instance.activate:
        HomeController.objects.filter(activate=True).update(activate=False)
        
@receiver(pre_save,sender = FestivalSale)
def deactive_festival_previous(sender,instance,*args, **kwargs):
    if instance.activate:
        FestivalSale.objects.filter(activate=True).update(activate=False)