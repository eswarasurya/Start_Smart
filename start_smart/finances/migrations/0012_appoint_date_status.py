# Generated by Django 3.0.8 on 2020-07-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0011_auto_20200716_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='appoint_date',
            name='status',
            field=models.CharField(choices=[('open', 'OPEN'), ('closed', 'CLOSED')], default='open', max_length=20),
        ),
    ]