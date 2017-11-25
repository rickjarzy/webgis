from django.db import models

# Create your models here.

class Produkt(models.Model):

    name = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)


class Company(models.Model):

    name = models.CharField(max_length=200, null=True)

