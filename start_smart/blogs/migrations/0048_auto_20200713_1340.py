# Generated by Django 3.0.8 on 2020-07-13 13:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0047_auto_20200713_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 13, 13, 40, 56, 573050)),
        ),
    ]