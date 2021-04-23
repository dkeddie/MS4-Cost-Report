# Generated by Django 3.1.7 on 2021-04-22 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeAttachments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(blank=True, upload_to='change/attachments/')),
            ],
        ),
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_name', models.CharField(max_length=50, verbose_name='Change Name')),
                ('change_status', models.CharField(choices=[('A', 'Accepted'), ('P', 'Pending'), ('WiP', 'Work in Progress'), ('R', 'Rejected')], max_length=20, verbose_name='Change Status')),
                ('change_cost', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Change Cost')),
                ('attachment', models.ManyToManyField(blank=True, related_name='attachments', to='dashboard.ChangeAttachments')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('project_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
