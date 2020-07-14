# Generated by Django 3.0.8 on 2020-07-12 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='finances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.IntegerField(default=0)),
                ('Expenditure', models.TextField(default=0)),
                ('transactions', models.TextField()),
                ('threshold', models.IntegerField()),
                ('Budget', models.IntegerField()),
                ('Surplus', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]