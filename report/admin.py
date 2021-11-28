from django.contrib import admin
from .models import (
    Unit,
    ReportField,
    ReportSnapshot,
    FieldType,
    Period,
    ReportFieldValue,
    ReportSnapshotStatus,
    VisualizationType,
    Report
)

admin.site.register(Unit)
admin.site.register(ReportSnapshot)
admin.site.register(FieldType)
admin.site.register(Period)
admin.site.register(ReportFieldValue)
admin.site.register(ReportSnapshotStatus)
admin.site.register(VisualizationType)


class ReportTabularInline(admin.TabularInline):
    model = ReportField
    extra = 0
    prepopulated_fields = {'machine_name': ('name',)}


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    inlines = [ReportTabularInline]


@admin.register(ReportField)
class ReportFieldAdmin(admin.ModelAdmin):
    prepopulated_fields = {'machine_name': ('name',)}
