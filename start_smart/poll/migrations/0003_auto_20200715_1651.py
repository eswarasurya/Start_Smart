# Generated by Django 3.0.2 on 2020-07-15 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='ip_add',
            new_name='name',
        ),
    ]
