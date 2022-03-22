from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from .models import Collection, Product
from .serializers import CollectionSerializer, ProductSerializer
from store import serializers
# Create your views here.


class ProductList(ListCreateAPIView):
    # if we have complex querySet then we have to implement that in get_queryset() method
    def get_queryset(self):
        return Product.objects.all()

    # if we have complex serializer then we have to implement that in get_serializer_class
    def get_serializer_class(self):
        return ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class ProductDetail(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Product.objects.all()

    def get_serializer_class(self):
        return ProductSerializer

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.orderitems.count() > 0:
            return Response({'error': 'Product cannot be deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# this can be done like ProductList but as there is no complex query and serializer we can simply
# create this attributes


class CollectionList(ListCreateAPIView):

    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CollectionDetail(RetrieveUpdateDestroyAPIView):

    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
