from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=110)

    def __str__(self):
        return self.title
