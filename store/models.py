from tkinter import CASCADE
from django.db import models

# Create your models here.
class Promotion(models.Model) :
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model) :
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+')
    def __str__(self) -> str :
        return self.title
    class Meta:
        ordering = ['title']

class Product (models.Model) :
    title  = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']


class Customer(models.Model) :
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE,'BRONZE'),
        (MEMBERSHIP_SILVER,'SILVER'),
        (MEMBERSHIP_GOLD,'GOLD')
    ]
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    class Meta :
        ordering = ['first_name','last_name']
    

class Order(models.Model) :
    PAYMENT_FAILED = 'F'
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETED = 'C'
    PAYMENT_STATUS = [
        (PAYMENT_FAILED , 'FAILED'),
        (PAYMENT_PENDING , 'PENDING'),
        (PAYMENT_COMPLETED , 'COMPLETED')
    ]
    placed_at = models.DateTimeField(auto_now=True)
    payment_status = models.CharField(max_length=1,choices=PAYMENT_STATUS,default=PAYMENT_PENDING)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)

class Address(models.Model) :
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)


class OrderItem(models.Model) :
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT,related_name='orderitems')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)


class Cart(models.Model) :
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model) :
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)