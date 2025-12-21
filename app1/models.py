from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(models.Model):
    email = models.EmailField(max_length=255)
    password_hash = models.TextField()
    role = models.ForeignKey(
        to=Role, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.email
    
class Categories(models.Model):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to="categories")
    
    def __str__(self):
        return self.category_name

    
class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=150)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    vehicle_desc = models.TextField()
    fuel_type = models.CharField(max_length=50)
    seater = models.PositiveIntegerField()
    engine = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    vehicle_pic = models.ImageField(upload_to="vehicles")
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.vehicle_name