# Generated by Django 3.0.2 on 2020-03-10 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0020_auto_20200309_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 10, 23, 23, 51, 260626)),
        ),
    ]
