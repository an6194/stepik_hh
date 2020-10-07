from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy

from app_vacancy.models import Specialty, Vacancy


class Application(models.Model):
    written_username = models.CharField(max_length=120, verbose_name='Вас зовут')
    written_phone = models.CharField(max_length=120, verbose_name='Ваш телефон')
    written_cover_letter = models.TextField(verbose_name='Сопроводительное письмо')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")


class Resume(models.Model):
    class WorkStatusChoices(models.TextChoices):
        NOT_IN_SEARCH = 'NIS', gettext_lazy('Не ищу работу')
        CONSIDERATION = 'C', gettext_lazy('Рассматриваю предложения')
        IN_SEARCH = 'IS', gettext_lazy('Ищу работу')

    class GradeChoices(models.TextChoices):
        INTERN = 'intern', gettext_lazy('Стажер')
        JUNIOR = 'junior', gettext_lazy('Джуниор')
        MIDDLE = 'middle', gettext_lazy('Миддл')
        SENIOR = 'senior', gettext_lazy('Синьор')
        LEAD = 'lead', gettext_lazy('Лид')

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="resume")
    name = models.CharField(max_length=120, verbose_name='Имя')
    surname = models.CharField(max_length=120, verbose_name='Фамилия')
    status = models.CharField(max_length=80, choices=WorkStatusChoices.choices, verbose_name='Готовность к работе')
    salary = models.PositiveIntegerField(verbose_name='Ожидаемое вознаграждение')
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="resumes",
                                  verbose_name='Специальность')
    grade = models.CharField(max_length=80, choices=GradeChoices.choices, verbose_name='Квалификация')
    education = models.TextField(verbose_name='Образование')
    experience = models.TextField(verbose_name='Опыт работы')
    portfolio = models.CharField(max_length=120, verbose_name='Ссылка на портфолио')
