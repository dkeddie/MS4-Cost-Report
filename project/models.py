from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(
        "Project Name", max_length=20, null=False, blank=False)
    project_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    project_users = models.ManyToManyField(
        User, related_name='p_users', through='ProjectUser')
    original_estimate = models.DecimalField(
        "Estimate/Budget", default=0, max_digits=15, decimal_places=2, null=False, blank=False)
    has_subscription = models.BooleanField(
        default=False, blank=True, null=True)

    def __str__(self):
        return self.project_name


class ProjectUser(models.Model):
    PERMISSIONS = (
        ('Edit', 'Edit'),
        ('View', 'View'),
    )
    project_user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_permission = models.CharField(
        max_length=4, choices=PERMISSIONS, null=False, blank=False)

    def __str__(self):
        return self.project_user.username




