from django.db import models
from customers.models import customer
from products.models import  product
# data models for order
class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICES=((ORDER_PROCESSED,"ORDER_PROCESSED"),(ORDER_DELIVERED,"ORDER_DELIVERED"),(ORDER_REJECTED,"ORDER_REJECTED"))
    order_status=models.IntegerField(choices=STATUS_CHOICES,default=CART_STAGE)
    owner=models.ForeignKey(customer,on_delete=models.SET_NULL,null=True,related_name='order')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "order-{}-{}".format(self.id,self.owner.name)
#model for ordered items
class OrderedItem(models.Model):
    product=models.ForeignKey(product,related_name='added_cart',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')
