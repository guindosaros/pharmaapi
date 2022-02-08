from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin, ImportExportMixinBase
from medocapi import models


class ImportMixin(ImportExportMixinBase):
    """
    Import mixin.
    """

    from_encoding = "utf-8-sig"


class MedicamentsResource(resources.ModelResource):
    class Meta:
        model = models.Medicaments
        fields = (
            "id",
            "code",
            "nom",
            "dci1",
            "dosage1",
            "unite_dosage1",
            "forme",
            "presentation",
            "ppv",
            "ph",
            "prix_br",
            "principe_genetique",
            "taux_remboursement",
        )


class MedicamentsAdmin(ImportExportModelAdmin):
    from_encoding = "utf-8"
    resource_class = MedicamentsResource


# @admin.register(models.Medicaments)
# class MedicamentsAdmin(admin.ModelAdmin, MedicamentsResource):
#     resource_class = MedicamentsResource
#     list_display = (
#         "code",
#         "nom",
#         "ppv",
#         "status",
#         "date_add",
#         "date_upd",
#     )
#     list_filter = (
#         "status",
#         "date_add",
#         "date_upd",
#     )
#     list_per_page = 50
#     date_hierarchy = "date_add"


admin.site.register(models.Medicaments, MedicamentsAdmin)
