from django.contrib import admin
from .models import Change, ChangeAttachments

# Register your models here.

admin.site.register(Change)
admin.site.register(ChangeAttachments)