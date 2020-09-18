# Generated by Django 3.1.1 on 2020-09-18 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_vacancy', '0002_auto_20200914_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(verbose_name='Описание вакансии'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_max',
            field=models.PositiveIntegerField(verbose_name='Зарплата до'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_min',
            field=models.PositiveIntegerField(verbose_name='Зарплата от'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='skills',
            field=models.CharField(max_length=120, verbose_name='Требуемые навыки'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='app_vacancy.specialty', verbose_name='Специальность'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Название вакансии'),
        ),
    ]
