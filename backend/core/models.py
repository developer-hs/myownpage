from django.db import models


class TimestampedModel(models.Model):
    datetime_update = models.DateTimeField(auto_now=True)
    datetime_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-datetime_update', '-datetime_created']
