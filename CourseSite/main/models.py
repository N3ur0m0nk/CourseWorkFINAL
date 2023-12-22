import datetime
from django.db import models


# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name


class Item(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    Date = models.DateField(auto_now=True)
    FullFIO = models.TextField(max_length=100, default='')
    FIO = models.TextField(max_length=100, default='')
    Specialty = models.TextField(max_length=100, default='')
    FullKafedra = models.TextField(max_length=100, default='')
    Kafedra = models.TextField(max_length=100, default='')
    Birthday = models.DateField(default=datetime.date.today)
    Passport_Number = models.TextField(max_length=100, default='')
    Passport_Vidacha = models.TextField(max_length=100, default='')
    Passport_Date = models.DateField(default=datetime.date.today)
    Registration_Address = models.TextField(max_length=100, default='')

    def __str__(self):
        return self.FullFIO


class Form1(models.Model):
    name = models.CharField(max_length=100)
    Date = models.DateField(default=datetime.date.today)
    FullFIO = models.TextField(max_length=100)
    FIO = models.TextField(max_length=100)
    Specialty = models.TextField(max_length=100)
    FullKafedra = models.TextField(max_length=100)
    Kafedra = models.TextField(max_length=100)
    Birthday = models.DateField(default=datetime.date.today)
    Passport_Number = models.TextField(max_length=100)
    Passport_Vidacha = models.TextField(max_length=100)
    Passport_Date = models.DateField(default=datetime.date.today)
    Registration_Address = models.TextField(max_length=100)

    def __str__(self):
        return self.name
