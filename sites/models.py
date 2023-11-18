from django.db import models
from django.urls import reverse


class Site(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("site_detail", kwargs={"pk": self.pk})
