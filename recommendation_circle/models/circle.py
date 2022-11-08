from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from recommendation_circle.models import Profile


class Circle(models.Model):
    name = models.CharField(max_length=255)
    participants = models.ManyToManyField(Profile, related_name='circles', blank=True)
    last_edition = models.IntegerField(default=0)

    def __str__(self):
        return f"[{self.id}] {self.name}"


@receiver(post_save, sender="recommendation_circle.Edition")
def increment_circle_last_edition(sender, edition, created, **kwargs):
    if created:
        circle = edition.circle
        circle.last_edition += 1
        circle.save()
