# Generated by Django 2.0.7 on 2018-09-09 18:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_card', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='inn',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]{10}$')], verbose_name='ИНН'),
        ),
    ]
