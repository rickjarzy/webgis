from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Produkt
from .serializer import ProduktSerializer
# Create your views here.



def hello_world(request):
    return HttpResponse("Hello world, es geht bis jetzt")

# Lists all or create new one
# produkt/
class ProduktList(APIView):

    def get(self, request):

        prods = Produkt.objects.all()
        serializer = ProduktSerializer(prods, many=True)

        return Response(serializer.data)

    def post(self):
        pass















