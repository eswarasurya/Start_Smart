# Generated by Django 3.0.8 on 2020-07-16 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finances', '0010_auto_20200716_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoint_date',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]