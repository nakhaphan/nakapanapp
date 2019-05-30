from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=80)
    Locate = models.CharField(max_length=15)
