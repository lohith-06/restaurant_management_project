# from django.db import models

# # Create your models here.
# class Item(models.Model):
#     item_name = models.CharField(max_length=150)
#     item_price = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.item_name)\
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200, default="My Restaurant")
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    # Store opening hours as JSON (flexible for multiple days/times)
    opening_hours = models.JSONField(default=dict)  

    def __str__(self):
        return self.name