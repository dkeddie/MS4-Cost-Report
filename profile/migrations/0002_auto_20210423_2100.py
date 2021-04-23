# Generated by Django 3.1.7 on 2021-04-23 20:00

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubscriptiondetails',
            name='default_country',
            field=django_countries.fields.CountryField(default='', max_length=2, verbose_name='Country'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usersubscriptiondetails',
            name='default_county',
            field=models.CharField(default='', max_length=80, verbose_name='County'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usersubscriptiondetails',
            name='default_phone_number',
            field=models.CharField(default='', max_length=20, verbose_name='Phone Number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usersubscriptiondetails',
            name='default_postcode',
            field=models.CharField(default='', max_length=20, verbose_name='Post Cost'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usersubscriptiondetails',
            name='default_street_address1',
            field=models.CharField(default='', max_length=80, verbose_name='Street Address 1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usersubscriptiondetails',
            name='default_street_address2',
            field=models.CharField(default='', max_length=80, verbose_name='Street Address 2'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usersubscriptiondetails',
            name='default_town_or_city',
            field=models.CharField(default='', max_length=40, verbose_name='Town/City'),
            preserve_default=False,
        ),
    ]
