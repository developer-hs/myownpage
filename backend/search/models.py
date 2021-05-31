from django.db import models
from django.db.models.fields.related import ForeignKey
from core.models import TimestampedModel


class SearchHistory(TimestampedModel):
    search_term = models.CharField(max_length=120)
    user = ForeignKey(
        "users.User", related_name="search_history", on_delete=models.CASCADE)
