# code
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from users.models import UserProfile, Users

@receiver(post_save, sender=Users)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
  
@receiver(post_save, sender=Users)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()