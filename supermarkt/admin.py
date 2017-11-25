from django.contrib import admin
from .models import *
# Register your models here.

class ProduktAdmin(admin.ModelAdmin):

    list_display = ('name', 'price')


class ProduktTypeAdmin(admin.ModelAdmin):

    list_display = ('name',)

class CompanyAdmin(admin.ModelAdmin):

    list_display = ('name',)


admin.site.register(Produkt, ProduktAdmin)
admin.site.register(ProduktType, ProduktTypeAdmin)
admin.site.register(Company, CompanyAdmin)