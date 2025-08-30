# Create your models here.

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} ({self.email})"k {self.id} - {self.created_at.strftime('%Y-%m-%d')}"