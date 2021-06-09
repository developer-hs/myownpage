from core.models import TimestampedModel
from core.models import models

class NotePads(TimestampedModel):
    memo = models.TextField(blank=True)
    user = models.ForeignKey("users.User" , related_name="notepads" ,on_delete=models.CASCADE)
    done = models.BooleanField(default=False)