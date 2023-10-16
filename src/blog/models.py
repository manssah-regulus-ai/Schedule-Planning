from django.db import models

# Create your models here.

class Collaborator(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    age = models.IntegerField(default=0)
    annee = models.IntegerField(default=0)
    job = models.CharField(max_length=128)
    job_description = models.TextField(blank=True)
    magasin = models.CharField(max_length=128)
    thumbnail = models.ImageField(upload_to="collaborators", blank=True, null=True)
    def __str__(self):
        return f"{self.name}: {self.job}"
