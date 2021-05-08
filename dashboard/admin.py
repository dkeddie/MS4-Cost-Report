from django.contrib import admin
from .models import Change, ChangeAttachments


class AttachmentInline(admin.TabularInline):
    model = Change.attachment.through


class ChangeAdmin(admin.ModelAdmin):
    # model = Change
    list_display = [
        'project_id',
        'change_name'
    ]
    inlines = [
        AttachmentInline,
    ]


class AttachmentAdmin(admin.ModelAdmin):
    inlines = [
        AttachmentInline,
    ]
    exclude = ('attachment')


admin.site.register(Change, ChangeAdmin)