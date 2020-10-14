from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название компании')
    location = models.CharField(max_length=120, verbose_name='География')
    logo = models.ImageField(
        upload_to=settings.MEDIA_COMPANY_IMAGE_DIR,
        height_field='height_field',
        width_field='width_field',
        verbose_name='Логотип',
        default='default.gif'
    )
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)
    description = models.TextField(verbose_name='Информация о&nbsp;компании')
    employee_count = models.CharField(max_length=80, verbose_name='Количество человек в компании')
    owner = models.OneToOneField(User, on_delete=models.CASCADE,
                                 related_name="company", verbose_name='Владелец компании')
