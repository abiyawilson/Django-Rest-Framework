from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    phone = PhoneNumberField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.firstName + " " + self.lastName


class Order(models.Model):
    product = models.CharField(max_length=20)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
