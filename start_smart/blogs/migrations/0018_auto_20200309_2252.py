# Generated by Django 3.0.2 on 2020-03-09 17:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0017_auto_20200308_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 9, 22, 52, 20, 180493)),
        ),
    ]
