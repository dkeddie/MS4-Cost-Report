# Generated by Django 3.1.7 on 2021-04-22 18:46

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
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=20, verbose_name='Project Name')),
                ('original_estimate', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Estimate/Budget')),
                ('has_subscription', models.BooleanField(blank=True, default=False, null=True)),
                ('project_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_permission', models.CharField(choices=[('Edit', 'Edit'), ('View', 'View')], max_length=4)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('project_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='project_users',
            field=models.ManyToManyField(related_name='p_users', through='project.ProjectUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
