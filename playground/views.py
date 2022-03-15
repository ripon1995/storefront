from django.http import HttpResponse
from store.models import Product

# Create your views here.
def say_hello(request) :
    products = Product.objects.filter(unit_price__range=(20,30))
    return HttpResponse(list(products))