# Generated by Django 3.1.1 on 2020-09-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0003_auto_20200914_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='written_cover_letter',
            field=models.TextField(verbose_name='Сопроводительное письмо'),
        ),
        migrations.AlterField(
            model_name='application',
            name='written_phone',
            field=models.CharField(max_length=120, verbose_name='Ваш телефон'),
        ),
        migrations.AlterField(
            model_name='application',
            name='written_username',
            field=models.CharField(max_length=120, verbose_name='Вас зовут'),
        ),
    ]
