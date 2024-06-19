from django.db import models
from django.contrib.auth.models import User
from category.models import Category


class Choice:
    WORTHINESS = (('G', 'GOLD'), ('S', 'SLIVER'), ('B', 'BRONZE'))
    LEVEL = (('H', 'HIGH'), ('M', 'MEDIUM'), ('L', 'LOW'))


class Article(models.Model):
    title = models.CharField(max_length=40, verbose_name='Subject')
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    worthiness = models.CharField(max_length=10, choices=Choice.WORTHINESS)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    image = models.ImageField(upload_to='blog/articles/', null=True, blank=True)
    article = models.Manager()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField(default=18)
    email = models.EmailField()
    phone = models.PositiveIntegerField(default=989, help_text='without 09')
    level = models. CharField(choices=Choice.LEVEL, max_length=10)
    face = models.ImageField(null=True, blank=True)
    author = models.Manager()

    class Meta:
        ordering = ['age']
        verbose_name = 'Writer'
        verbose_name_plural = 'Writers'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"