from rest_framework import serializers
from .models import Produkt, ProduktType, Company


class ProduktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkt
        #fields = ('name', 'price')
        fields = '__all__'

