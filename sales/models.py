from django.db import models
from django.contrib.auth.models import User

class Sale(models.Model):
    user = models.ForeignKey(User, related_name="sales", on_delete=models.CASCADE)
    client = models.CharField(max_length=100)
    product = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.product
