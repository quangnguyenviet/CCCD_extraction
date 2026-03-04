from django.contrib import admin
from .models import IDCardRecord


@admin.register(IDCardRecord)
class IDCardRecordAdmin(admin.ModelAdmin):
    list_display = (
        "id_number",
        "full_name",
        "date_of_birth",
        "gender",
        "status",
        "created_at",
    )
    list_filter = ("status", "gender")
    search_fields = ("id_number", "full_name")