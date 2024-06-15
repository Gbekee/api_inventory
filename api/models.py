from django.db import models
from datetime import date
class Supplier(models.Model):
    name=models.CharField(max_length=255)
    contact=models.EmailField(unique=True)
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    date_added=models.DateField(default=date.today)
    suppliers=models.ManyToManyField(Supplier, related_name='items')
    def __str__(self):
        return self.name