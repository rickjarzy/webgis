from django.db import models

# Create your models here.


class Produkt(models.Model):

    class Meta:
        verbose_name_plural = "Produkte"
        db_table = 'webgis_produkt'

    name = models.CharField(max_length=200, null=True, blank=True)
    company = models.ForeignKey('Company', null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    type = models.ForeignKey('ProduktType', null=True, blank=True)

    


class Company(models.Model):
    class Meta:
        db_table = 'webgis_company'
        verbose_name_plural = "Companies"

    name = models.CharField(max_length=200, null=True, blank=True)
    position_x = models.CharField(max_length=200, null=True, blank=True)
    position_y = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.name)
    

class ProduktType(models.Model):
    class Meta:
        db_table = 'webgis_produkttype'
        verbose_name_plural = "Produkttypen"

    name = models.CharField(max_length=200, null=True, blank=True)
    tiefkuehl = models.CharField(max_length=200, null=True, blank=True)


