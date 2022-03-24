from django.db import models


# Create your models here.
class Passanger(models.Model):
    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    rewardPoints = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        ordering = ['id']
