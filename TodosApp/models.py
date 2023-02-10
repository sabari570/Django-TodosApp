from django.db import models
from datetime import datetime

# Create your models here.
class Task(models.Model):
    taskname = models.CharField(max_length=10000)
    taskCreated = models.DateField(default=datetime.now, blank=True)

