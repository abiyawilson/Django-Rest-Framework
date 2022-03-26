from django.db import models


# Create your models here.
class Course(models.Model):

    id = models.IntegerField(primary_key=True)
    course = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    ratings = models.IntegerField(default=1)

    class Meta:
        ordering = ['id']
