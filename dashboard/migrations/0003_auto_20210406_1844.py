# Generated by Django 3.1.7 on 2021-04-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20210405_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changeattachments',
            name='attachment',
            field=models.FileField(blank=True, upload_to='change/attachments/'),
        ),
    ]
