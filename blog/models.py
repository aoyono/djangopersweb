from django.db import models
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    titre = models.CharField(max_length=200)
    texte = models.TextField()
    date_creation = models.DateTimeField(default=timezone.now)
    date_publication = models.DateTimeField(blank=True, null=True)

    def publier(self):
        self.date_publication = timezone.now()
        self.save()

    def __str__(self):
        return self.titre
