# # Create your models here.
# # models.py
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
from django.db import models

class RestaurantLocation(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} {self.zip_code}"
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)  # New field

    def __str__(self):
        return self.name
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # ✅ new field

    def __str__(self):
        return self.name
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
        
class OpeningHour(models.Model):
    day = models.CharField(max_length=20)
    open_time = models.TimeField()
    close_time = models.TimeField()

    # def __str__(self):
        return f"{self.day}: {self.open_time} - {self.close_time}"
class TodaySpecial(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.item_name
class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)

    def __str__(self):
        return self.title
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    feedback = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.submitted_at.strftime('%Y-%m-%d')}"
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    category = models.CharField(max_length=50, blank=True)

    def __str__(self):
#         return self.name
# from django.db import models

# class Category(models.Model):
#     category_name = models.CharField(max_length=100, unique=True)

#     def __str__(self):
#         return self.category_name


# class MenuItem(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     is_available = models.BooleanField(default=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menu_items')

#     def __str__(self):
#         return self.name