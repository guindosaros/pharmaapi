from django.contrib import admin
from medocapi import models


@admin.register(models.Medicaments)
class MedicamentsAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "nom",
        "ppv",
        "status",
        "date_add",
        "date_upd",
    )
    list_filter = (
        "status",
        "date_add",
        "date_upd",
    )
    list_per_page = 50
    date_hierarchy = "date_add"
