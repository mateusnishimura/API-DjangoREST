from pyexpat import model
from rest_framework import serializers
from frexco.models import Fruit, Region
from django.forms import ValidationError


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = '__all__'