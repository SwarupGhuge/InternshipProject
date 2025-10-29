from django.db import models

# Create your models here.
class HRMmodel(models.Model):
    Department_name = models.CharField(max_length=20)
    Department_description = models.CharField(max_length=20)
