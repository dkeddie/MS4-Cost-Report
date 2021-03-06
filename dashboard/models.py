from django.db import models
from django.contrib.auth.models import User
from project.models import Project

from django.conf import settings

import os


class ChangeAttachments(models.Model):
    attachment = models.FileField(upload_to='change/attachments/', blank=True)

    def delete(self, *args, **kwargs):
        self.attachment.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        name_full = str(self.attachment)
        name = name_full.split("/")
        return str(name[-1])


class Change(models.Model):
    CHANGE_STATUS = (
        ('A', 'Accepted'),
        ('P', 'Pending'),
        ('WiP', 'Work in Progress'),
        ('R', 'Rejected'),
    )
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    project_user = models.ForeignKey(User, on_delete=models.CASCADE)
    change_name = models.CharField(
        "Change Name", max_length=40, null=False, blank=False)
    change_status = models.CharField(
        "Change Status", max_length=20, choices=CHANGE_STATUS, null=False, blank=False)
    change_cost = models.FloatField(
        "Change Cost", default=0, null=False, blank=False)
    attachment = models.ManyToManyField(
        ChangeAttachments, related_name="attachments", blank=True)

    def __str__(self):
        return self.change_name
