# Generated by Django 3.1.1 on 2020-09-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0008_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='portfolio',
            field=models.CharField(max_length=120, verbose_name='Ссылка на портфолио'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='salary',
            field=models.PositiveIntegerField(verbose_name='Ожидаемое вознаграждение'),
        ),
    ]
