from django.db import models

# Create your models here.

class Internationals(models.Model):
    InternationalId = models.AutoField(primary_key=True)
    InternationalName = models.CharField(max_length=500)

class Locals(models.Model):
    LocalId = models.AutoField(primary_key=True)
    LocalName = models.CharField(max_length=500)

class Scholarship(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()