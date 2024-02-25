from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name    
class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.TextField()
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    photo = models.ImageField(upload_to='dishes/')
    def __str__(self):
        return self.name
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    working_hours = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.name
