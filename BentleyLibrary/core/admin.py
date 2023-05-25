import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Bookinventory, Log

def export_book_inventory(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="book_inventory.csv"'

    writer = csv.writer(response)
    writer.writerow([field.name for field in Bookinventory._meta.fields])  # Export all field names

    for book in queryset:
        writer.writerow([getattr(book, field.name) for field in Bookinventory._meta.fields])  # Export all field values

    return response

def export_log(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="log.csv"'

    writer = csv.writer(response)
    writer.writerow([field.name for field in Log._meta.fields])  # Export all field names

    for log_entry in queryset:
        writer.writerow([getattr(log_entry, field.name) for field in Log._meta.fields])  # Export all field values

    return response

export_book_inventory.short_description = "Export selected book inventory as CSV"
export_log.short_description = "Export selected log entries as CSV"

@admin.register(Bookinventory)
class BookInventoryAdmin(admin.ModelAdmin):
    actions = [export_book_inventory]

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    actions = [export_log]
