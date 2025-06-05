from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
import datetime
from django.urls import reverse



# Create your views here.

def store(request):
  products = Product.objects.all()

  if request.user.is_authenticated:
    if not Customer.objects.filter(user=request.user).exists():
      Customer.objects.create(user=request.user)
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, order_complete=False)
    items = order.orderitem_set.all()
    cart_items = order.get_amount()
  else:
    items = []
    order = {'get_total': 0, 'get_amount': 0}
    cart_items = order['get_amount']
  
  return render(request, './store.html', {
    'products': products,
    'cartItems': cart_items
    })

def cart(request):
  products = Product.objects.all()

  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, order_complete=False)
    items = order.orderitem_set.all()
  else:
    items = []
    order = {'get_total': 0, 'get_amount': 0}
  
  return render(request, './cart.html', {
    'items': items,
    'order': order,
  })

def checkout(request):
  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, order_complete=False)
    items = order.orderitem_set.all()
  else:
      items = []
      order = {'get_total': 0, 'get_amount': 0}


  return render(request, './checkout.html', {
    'items': items,
    'order': order,
    })


def updateItem(request):
  data = json.loads(request.body)
  productId = data['productId']
  action = data['action']

  customer = request.user.customer
  product = Product.objects.get(id=productId)
  order, created = Order.objects.get_or_create(customer=customer, order_complete=False)
  orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

  if action == 'remove':
    print('removing button')
    orderItem.delete()


def processOrder(request):
  print('requesting prder')
  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, order_complete=False)
    order.order_id = datetime.datetime.now().timestamp()
    order.order_complete = True
    order.save()