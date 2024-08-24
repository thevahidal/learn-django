from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    pages = models.IntegerField(default=0)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    is_active = models.BooleanField(default=True)
