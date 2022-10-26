from random import choices
from django.db import models

# Create your models here.

CHOICE = (("danger", "high"), ("warning", "normal"), ("info", "low"))


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(max_length=50, choices=CHOICE)
    deadline = models.DateField()

    def __str__(self):
        return self.title
