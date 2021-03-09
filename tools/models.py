from django.db import models


class Birthday(models.Model):
    person = models.CharField(max_length=100, primary_key=True)
    message = models.TextField(max_length=1000)
    # Yes, there is no encryption here: bazinga.
    password = models.CharField(max_length=100, default='password')

    def __str__(self):
        return self.person
