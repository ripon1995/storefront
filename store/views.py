from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin
from rest_framework import status
from .models import Collection, OrderItem, Product, Review,Cart
from .serializers import CartSerializer, CollectionSerializer, ProductSerializer, ReviewSerializer
# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product cannot be deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class ReviewViewSet(ModelViewSet):
    
    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    serializer_class = ReviewSerializer

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}


class CartViewSet(CreateModelMixin,GenericViewSet,RetrieveModelMixin):
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer
