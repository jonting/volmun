# Generated by Django 2.1.15 on 2020-01-31 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('committees', '0010_committee_docket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='committee',
            name='docket',
        ),
    ]