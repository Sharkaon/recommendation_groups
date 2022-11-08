from django.db import models
from recommendation_circle.models.circle import Circle


class Edition(models.Model):
    number = models.IntegerField()
    circle = models.ForeignKey(Circle, related_name='editions', on_delete=models.CASCADE)
    order = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"[{self.id}] {self.number}º of {self.circle.name}"
