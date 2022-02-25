from django.contrib import admin
from django.utils.safestring import mark_safe
from medocapi import models


class Action(admin.ModelAdmin):

    date_hierarchy = "date_add"
    ordering = ("-date_upd",)
    list_filter = ("status",)
    list_per_page = 10

    actions = ("active", "desactive")

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "Activer les elements selectionner")

    active.short_description = "active elements"

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "Desactiver les elements selectionner")

    desactive.short_description = "desactive elements"


@admin.register(models.Category)
class CategoryAdmin(Action):

    list_display = (
        "view_image",
        "nom",
        "date_add",
        "date_upd",
        "status",
    )
    list_filter = (
        "date_add",
        "date_upd",
        "status",
    )
    list_display_links = ("view_image",)

    def view_image(self, obj):
        try:
            return mark_safe(
                '<img src = "{url}" width ="100px" height ="100px" />'.format(
                    url=obj.image.url
                )
            )
        except Exception as e:
            print(e)
