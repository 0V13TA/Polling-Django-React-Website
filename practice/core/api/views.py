from rest_framework import generics

from .serializers import ProductSerializer
from .models import Product

# Create your views here.


class ProductDetailApiView(generics.RetrieveAPIView):
    pass
