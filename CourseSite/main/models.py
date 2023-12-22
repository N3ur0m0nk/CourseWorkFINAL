import datetime
from django.db import models


# Create your models here.
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
