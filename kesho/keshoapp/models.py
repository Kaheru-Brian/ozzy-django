from django.db import models
from django.utils import timezone
# Create your models here.

class Categorystay(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Pay(models.Model):
    payment_cat = models.ForeignKey(Categorystay, on_delete=models.CASCADE, null=True, blank=True)
    pay_number = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField( null=True, blank=True)
    currency = models.CharField( max_length=5, default="UGX", blank=True, null=True)

    def __int__(self):
        return self.currency
    
    
    
class Babe(models.Model):
    c_stay = models.ForeignKey(Categorystay, on_delete=models.CASCADE, null=True, blank=True)
    fee = models.ForeignKey(Pay, on_delete=models.CASCADE, null=True, blank=True)
    b_name = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True, default=1)
    gender = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True,blank=True)
    sponsor = models.CharField(max_length=200, null=True, blank=True)
    b_taker = models.CharField(max_length=200, null=True, blank=True)
    timein = models.DateTimeField(null=True, blank=True)
    timeout = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.b_name

