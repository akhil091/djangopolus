from django.db import models
import sys
from django.utils.timezone import now
from datetime import date

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=500)
    message = models.TextField()
    pub_date = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.name}"
