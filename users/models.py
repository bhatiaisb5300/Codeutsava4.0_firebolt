from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Crop(models.Model):
    crop_type = models.CharField(max_length=20,default=0)
    season = models.CharField(max_length=30,default=0)
    crop = models.CharField(max_length=20,default=0)
    crop_yield = models.IntegerField(default=0)

    def __str__(self):
        return self.crop

class User(AbstractUser):
    user_type   = models.BooleanField(default=False)
    phone = models.CharField(max_length=15,default=0)

    def __str__(self):
        return self.first_name


class Farmer(models.Model):
    crop = models.ManyToManyField(Crop)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    reg_no = models.CharField(max_length=20)
    land_area = models.IntegerField()
    # warehouse = models.BooleanField()

    def __str__(self):
        return self.first_name


class Shops(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name

class Mandi(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name

class Consumer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name

class Warehouse(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    silo_capacity = models.IntegerField()
    contact = models.CharField(max_length=15)
    available = models.IntegerField(default=0)
    additional = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class contact(models.Model):

    name = models.CharField(max_length=20,default='')
    phone = models.CharField(max_length=15,default='')
    email = models.EmailField(default='')
    subject = models.CharField(max_length=100,default='')
    message = models.CharField(max_length=1000,default='')

    def __str__(self):
        return self.name


class farmerPost(models.Model):

    images = models.ImageField(upload_to='posts/img')
    desc = models.CharField(max_length=200)
    warehouse = models.ForeignKey(Warehouse,on_delete=models.CASCADE,default='')
    crop = models.ForeignKey(Crop,on_delete=models.CASCADE)
    qty = models.IntegerField()
    price_kg = models.IntegerField()
    extra = models.CharField(max_length=500)
