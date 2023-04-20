from django.db import models
from django import forms

class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    done = models.BooleanField(default=False)