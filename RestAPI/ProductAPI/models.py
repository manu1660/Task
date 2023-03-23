from django.db import models

#Mobile Products#
# Create your models here.

class Products(models.Model):
    image=models.ImageField(null=True,upload_to="images")
    name=models.CharField(max_length=200)
    ram=models.CharField(max_length=100)
    storage=models.CharField(max_length=100)
    display=models.CharField(max_length=200)
    operating_system=models.CharField(max_length=200)
    processor=models.CharField(max_length=200)
    connectivity=models.CharField(max_length=200)
    rear_camera=models.CharField(max_length=200)
    front_camera=models.CharField(max_length=200)
    battery_charging=models.CharField(max_length=200)
    weight=models.CharField(max_length=200)
    price=models.IntegerField() 
    
    def __str__(self):
        return self.name
        