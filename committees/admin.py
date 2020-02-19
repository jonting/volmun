from django.contrib import admin

from .models import Committee, Topic


class TopicInline(admin.TabularInline):
    model = Topic
    extra = 2


class CommitteeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['abbr']}),
        (None,               {'fields': ['name']}),
        ('Description', {'fields': ['description']}),
        ('Is this a full crisis committee?', {'fields': ['full_crisis']}),
        ('Header Image', {'fields': ['header', ('header_x', 'header_y')]}),
        ('Thumbnail Image', {'fields': ['thumbnail']}),
        ('Background Guide', {'fields': ['background_guide']}),
        ('Docket', {'fields': ['docket']}),
        ('Dossier (if full crisis committee)', {'fields': ['dossier']}),
    ]
    inlines = [TopicInline]
    list_display = ('abbr', 'name', 'description', 'full_crisis')
    search_fields = ['abbr']


admin.site.register(Committee, CommitteeAdmin)
