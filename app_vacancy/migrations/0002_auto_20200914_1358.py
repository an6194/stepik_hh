# Generated by Django 3.1.1 on 2020-09-14 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_vacancy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialty',
            name='height_field',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='specialty',
            name='width_field',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.ImageField(height_field='height_field', upload_to='speciality_images', width_field='width_field'),
        ),
    ]