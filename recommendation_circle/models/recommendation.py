from django.db import models

    def __str__(self):
        from_str = self.from_user.name if self.from_user else self.from_user_name
        to_str = self.to_user.name if self.to_user else self.to_user_name

        return f"{from_str} recommended {self.anime} to {to_str}"
