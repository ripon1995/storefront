from store.models import Product,Collection
from decimal import Decimal
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','slug','description','inventory','unit_price','price_with_tax','collection']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self,product:Product):
        return product.unit_price * Decimal(1.1)


class CollectionSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Collection
        fields = ['id','title','featured_product']
    