from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Customer(models.Model):
   """
   Model created to store the customer's/user's details
   """
   user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
   name = models.CharField(max_length=200)
   email = models.CharField(max_length=200)

   def __str__(self):
      return self.name

class Product(models.Model):
    """
    Model created to store the product
    """
    name = models.CharField(max_length=200)
    price = models.FloatField()
    created = models.DateTimeField('date published', auto_now_add=True)
    image_link = models.URLField(default="https://placehold.co/600x400/png")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.name


class Order(models.Model):
  """
  Model created to store the user's orders
  """
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
  order_complete = models.BooleanField(default=False)
  order_id = models.CharField(max_length=200, default=0)

  def __str__(self):
      return str(self.id)
  
  @property
  def get_total(self):
     items = self.orderitem_set.all()
     total = sum([item.get_total() for item in items])
     return total
  
  def get_amount(self):
     items = self.orderitem_set.all()
     return len(items)

  
class OrderItem(models.Model):
  """
  Model created to store the ordered item
  """
  product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)

  def get_total(self):
    return self.product.price