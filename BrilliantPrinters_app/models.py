from django.db import models
from django.urls import reverse

# Create your models here.



class Question(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=200, blank=False)
    answered = models.BooleanField(default=False)