from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    logo = models.ImageField(
        upload_to=settings.MEDIA_COMPANY_IMAGE_DIR,
        height_field='height_field',
        width_field='width_field'
    )
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)
    description = models.TextField()
    employee_count = models.CharField(max_length=80)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="company")


class Application(models.Model):
    written_username = models.CharField(max_length=120)
    written_phone = models.CharField(max_length=120)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey('app_vacancy.Vacancy', on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
