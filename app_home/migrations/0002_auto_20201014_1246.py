# Generated by Django 3.1.1 on 2020-10-14 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='written_phone',
            field=models.CharField(max_length=120, verbose_name='Телефон отправителя'),
        ),
        migrations.AlterField(
            model_name='application',
            name='written_username',
            field=models.CharField(max_length=120, verbose_name='Имя отправителя'),
        ),
    ]