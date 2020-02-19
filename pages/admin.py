from django.contrib import admin

from .models import Branch, Staff, Position


class BranchAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Positions', {'fields': ['position']}),
    ]
    list_display = ('name',)
    search_fields = ['name']


class StaffAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['committee']}),
        ('Biography', {'fields': ['bio']}),
        ('Profile Picture', {'fields': ['picture']}),
    ]
    list_display = ('name', 'committee')
    search_fields = ['name']


class PositionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['priority']}),
        ('Staff', {'fields': ['staff']}),
    ]
    list_display = ('name', 'priority')
    search_fields = ['name']


admin.site.register(Branch, BranchAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Position, PositionAdmin)
