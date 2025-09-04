# Create your models here.
# models.py
# from django.db import models

# class MenuItem(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

#     def __str__(self):
#         return self.name# models.py
# models.py
# from django.db import models

# class MenuItem(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     image = models.ImageField(upload_to="menu_images/", blank=True, null=True)  # new field

#     def __str__(self):
#         return self.name# models.py
# from django.db import models

# class RestaurantLocation(models.Model):
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zip_code = models.CharField(max_length=20)

#     def __str__(self):
#         return f"{self.address}, {self.city}, {self.state} {self.zip_code}"
# from django.db import models

# class MenuItem(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     image = models.ImageField(upload_to='menu_images/', blank=True, null=True)  # New field

#     def __str__(self):
#         return self.name
# from django.db import models

# class Restaurant(models.Model):
#     name = models.CharField(max_length=200)
#     address = models.TextField()
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zip_code = models.CharField(max_length=10)
#     phone_number = models.CharField(max_length=15, blank=True, null=True)  # ✅ new field

#     def __str__(self):
#         return self.name
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    logo = models.ImageField(upload_to="restaurant_logos/", blank=True, null=True)  # ✅ new field

    def __str__(self):
        return self.name