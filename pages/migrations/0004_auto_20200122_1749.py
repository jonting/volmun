# Generated by Django 2.1.15 on 2020-01-22 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200122_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='staff',
            field=models.ManyToManyField(blank=True, null=True, related_name='positions', to='pages.Staff'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='committee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='committees.Committee'),
        ),
    ]