from django.db import models


class Link(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=250, name='href')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.name
