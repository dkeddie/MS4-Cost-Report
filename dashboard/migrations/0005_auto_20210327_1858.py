# Generated by Django 3.1.7 on 2021-03-27 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210325_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='change',
            name='change_status',
            field=models.CharField(choices=[('A', 'Accepted'), ('P', 'Pending'), ('WiP', 'Work in Progress'), ('R', 'Rejected')], max_length=20, verbose_name='Change Status'),
        ),
    ]
