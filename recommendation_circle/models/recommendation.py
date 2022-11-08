from django.db import models
from recommendation_circle.models import Profile, Edition


class Recommendation(models.Model):
    anime = models.CharField(max_length=255)
    from_user_name = models.CharField(max_length=255)
    to_user_name = models.CharField(max_length=255)
    edition = models.ForeignKey(
        Edition,
        on_delete=models.CASCADE,
        related_name='recommendations',
        blank=True,
        null=True
    )
    from_user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='recommendations_made',
        blank=True,
        null=True
    )
    to_user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='recommendations_received',
        blank=True,
        null=True
    )

    def __str__(self):
        from_str = self.from_user.name if self.from_user else self.from_user_name
        to_str = self.to_user.name if self.to_user else self.to_user_name

        return f"{from_str} recommended {self.anime} to {to_str}"
