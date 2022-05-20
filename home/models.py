from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(max_length=40, null=True)
    subscribed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
