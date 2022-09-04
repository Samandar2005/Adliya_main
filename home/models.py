from this import s
from turtle import back
from django.db import models


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='static/images/regions')

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=250)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    region_name = models.CharField(max_length=230)
    icon = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.region_name}, {self.name}"


class District(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='static/images/district')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SubDepartment(models.Model):
    name = models.CharField(max_length=250)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Posation(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Staff(models.Model):
    last_name = models.CharField(max_length=250, default='Anvar')
    first_name = models.CharField(max_length=250, default='Shokirov')
    age = models.IntegerField(default=0)
    img = models.ImageField(upload_to='static/images/staff')
    posation = models.ForeignKey(Posation, on_delete=models.CASCADE)
    subdepartment = models.ForeignKey(
        SubDepartment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
