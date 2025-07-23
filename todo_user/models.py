from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # NEW
    title = models.CharField(max_length=100)
    complated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.title
