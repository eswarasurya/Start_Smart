# Generated by Django 3.0.2 on 2020-07-15 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0049_auto_20200715_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 15, 15, 16, 17, 689989)),
        ),
    ]
