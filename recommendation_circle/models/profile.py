from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField()


@receiver(post_save, sender=User)
def create_user_profile(sender, user, created, **kwargs):
    if created:
        Profile.objects.create(user=user)


@receiver(post_save, sender=User)
def save_user_profile(sender, user, **kwargs):
    user.profile.save()
