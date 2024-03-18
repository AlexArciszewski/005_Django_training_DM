from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """buduje adres URL do danego widoku na podstawie podanej przez użytkownika nazwy. """
        return reverse('article-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title