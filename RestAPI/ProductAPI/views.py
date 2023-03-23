from django.shortcuts import render
from ProductAPI.models import Products
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import GenericViewSet
from ProductAPI.serializers import ProductModelSerializer
# Create your views here.


class ProductsCRUD(ModelViewSet):
    serializer_class=ProductModelSerializer
    queryset=Products.objects.all()
    