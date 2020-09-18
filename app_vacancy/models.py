from datetime import date

from django.conf import settings
from django.db import models


class Specialty(models.Model):
    code = models.CharField(max_length=80, unique=True)
    title = models.CharField(max_length=120)
    picture = models.ImageField(
        upload_to=settings.MEDIA_SPECIALITY_IMAGE_DIR,
        height_field='height_field',
        width_field='width_field'
    )
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)


class Vacancy(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название вакансии')
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies",
                                  verbose_name='Специальность')
    company = models.ForeignKey('app_home.Company', on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=120, verbose_name='Требуемые навыки')
    description = models.TextField(verbose_name='Описание вакансии')
    salary_min = models.IntegerField(verbose_name='Зарплата от')
    salary_max = models.IntegerField(verbose_name='Зарплата до')
    published_at = models.DateField(default=date.today)
