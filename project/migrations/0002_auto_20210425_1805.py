# Generated by Django 3.1.7 on 2021-04-25 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='original_estimate',
            field=models.FloatField(default=0, verbose_name='Estimate/Budget'),
        ),
    ]
