# Generated by Django 2.1.15 on 2020-01-22 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200122_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='branch_name',
            new_name='name',
        ),
    ]
