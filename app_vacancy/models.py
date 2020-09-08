from datetime import date

from django.db import models

from app_home.models import Company


class Specialty(models.Model):
    code = models.CharField(max_length=80)
    title = models.CharField(max_length=120)
    picture = models.CharField(max_length=120, default='https://place-hold.it/100x60')


class Vacancy(models.Model):
    title = models.CharField(max_length=120)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=120)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField(default=date.today)
