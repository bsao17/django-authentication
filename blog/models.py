from django.db import models


# Create your models here.
class Author(models.Model):
    article_numbers = models.IntegerField(default=0, blank=True, null=True)