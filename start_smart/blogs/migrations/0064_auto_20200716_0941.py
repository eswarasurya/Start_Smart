# Generated by Django 3.0.8 on 2020-07-16 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0063_auto_20200716_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 16, 9, 41, 25, 758938)),
        ),
    ]
