from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class StudentDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name