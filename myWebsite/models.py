from django.db import models

class MyTable(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone = models.IntegerField(null=True)
    time = models.DateField(null=True)


# Create your models here.
