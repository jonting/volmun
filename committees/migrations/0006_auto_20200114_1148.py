# Generated by Django 2.1.15 on 2020-01-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committees', '0005_auto_20200113_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='committee',
            name='background_guide',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='committee',
            name='dossier',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
