from django.db import models


class Recommendation(models.Model):
    anime = models.CharField(max_length=255)
    from_user_name = models.CharField(max_length=255)
    to_user_name = models.CharField(max_length=255)

    def __str__(self):
        from_str = self.from_user.name if self.from_user else self.from_user_name
        to_str = self.to_user.name if self.to_user else self.to_user_name

        return f"{from_str} recommended {self.anime} to {to_str}"
