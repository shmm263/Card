# Generated by Django 2.0.7 on 2018-09-11 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_card', '0004_auto_20180911_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medexamination',
            name='date_update',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_update',
            field=models.DateTimeField(null=True),
        ),
    ]