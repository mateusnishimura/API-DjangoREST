#from django.shortcuts import render
from django.forms import ValidationError
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets,status
from rest_framework.response import Response
from frexco.models import Fruit, Region
from frexco.serializer import FruitSerializer, RegionSerializer

class RegionsViewSet(viewsets.ModelViewSet):
    """Exibindo todas as regiões cadastradas"""
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class FruitsViewSet(viewsets.ModelViewSet):
    """Exibindo todas as frutas cadastradas"""
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer