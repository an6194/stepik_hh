from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    logo = models.CharField(max_length=120, default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()
