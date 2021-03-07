from django.db import models


class Birthday(models.Model):
    person = models.CharField(max_length=100, primary_key=True)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.person
