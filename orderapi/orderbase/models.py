#from __future__ import unicode_literals

from django.db import models

class UsersOrder(models.Model):
    user_name = models.CharField(max_length=100)
    user_login = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100, blank=True, default='')

    class Meta:
       db_table = u'users_order'

    def save(self, *args, **kwargs):
        return super(Users, self).save(*args, **kwargsi)


class Merchandise(models.Model):
    name_merch = models.CharField(max_length=50)
    merch_price = models.CharField(max_length=100,blank=True,default='')
    merch_count = models.CharField(max_length=100)
    merch_enabled = models.CharField(max_length=1)
    merch_del = models.CharField(max_length=1)
    image = models.FilePathField(null=True, blank=True)
    merch_description = models.TextField(blank=True, default='')

    class Meta:
        db_table = u'order_merch_cat'
    
    def save(self, *args, **kwargs):
        return super(Merchandise, self).save(*args, **kwargsi)


class Order(models.Model):
    order_num = models.IntegerField()
    order_user_id = models.ForeignKey(UsersOrder)
    order_description = models.TextField(blank=True, default='')
    order_state = models.CharField(max_length=1)
    order_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = u'order_info'

    def save(self, *args, **kwargs):
            
        return super(Order, self).save(*args, **kwargsi)


class OrderDetails(models.Model):  
    order_id = models.ForeignKey(Order)
    merch_id = models.ForeignKey(Merchandise)
    merch_sum = models.CharField(max_length=100)
    order_price = models.CharField(max_length=100)
    
    class Meta:
        db_table = u'order_details'


 
