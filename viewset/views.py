from rest_framework import viewsets
from .models import Products
from .serializers import ProductsSerializer
from django.shortcuts import render

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

# views.py











