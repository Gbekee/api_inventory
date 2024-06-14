from django.db import models
from datetime import date
class Supplier(models.Model):
    name=models.CharField(max_length=255)
    contact=models.EmailField(unique=True, blank=False)
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    price=models.FloatField()
    date_added=models.DateField(default=date.today, blank=True)
    suppliers=models.ManyToManyField(Supplier, related_name='items')
    def __str__(self):
        return self.name