from django.db import models

class InputSite(models.Model):
    name = models.CharField(max_length=180)
    site_url = models.URLField()

    def __str__(self):
        return self.name

class BookmarkSites(models.Model):
    sites = models.ManyToManyField("InputSite" , related_name="site" , blank=True)
    user = models.OneToOneField("users.User" , related_name="bookmark" , on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username