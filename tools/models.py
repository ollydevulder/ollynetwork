from django.db import models

from random import choice
from string import ascii_letters


def randomString(n, charset=ascii_letters):
    return ''.join([choice(charset) for _ in range(n)])


class Birthday(models.Model):
    person = models.CharField(max_length=100, primary_key=True)
    message = models.TextField(max_length=1000)
    # Yes, there is no encryption here: bazinga.
    password = models.CharField(max_length=100, default='password')

    def __str__(self):
        return self.person

class Short(models.Model):
    long_url = models.URLField(
        max_length=500,
        name='long',
        unique=True,
        blank=False,
    )
    short_url = models.CharField(
        max_length=4,
        name='short',
        primary_key=True,
        blank=False
    )

    def __str__(self):
        return self.long

    def save(self, *args, **kwargs):
        if not self.pk:
            short = False
            while not short:
                short = randomString(4)
                if len(Short.objects.filter(short=short)):
                    short = False
            self.short = short

        super().save(*args, **kwargs)
