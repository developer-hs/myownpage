from django.db import models

class Schedule(models.Model):
    name = models.CharField(max_length=80)
    start = models.DateTimeField()
    end = models.DateTimeField()
    color = models.CharField(max_length=80)
    timed = models.BooleanField()
    user = models.ForeignKey("users.User", related_name="schedule" , on_delete=models.CASCADE)