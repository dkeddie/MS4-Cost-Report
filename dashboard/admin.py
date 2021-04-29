from django.contrib import admin
from .models import Change, ChangeAttachments


admin.site.register(Change)


class AttachmentInline(admin.TabularInline):
    model = Change.attachment.through


class ChangeAdmin(admin.ModelAdmin):
    inlines = [
        AttachmentInline,
    ]


class AttachmentAdmin(admin.ModelAdmin):
    inlines = [
        AttachmentInline,
    ]
    exclude = ('attachment')
