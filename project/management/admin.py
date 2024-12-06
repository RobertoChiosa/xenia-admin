#  Copyright © Roberto Chiosa 2024.
#  Email: roberto@xeniapm.it
#  Last edited: 6/12/2024

# Third party imports
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

from .models import CadastralData, Host, Property


class HostAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "surname", "email", "fiscal_code"]
    fieldsets = [
        (
            None,
            {
                "fields": ["property"],
                # "classes": ["collapse"]
            },
        ),
        (
            _("Anagrafica"),
            {
                "fields": [
                    "name",
                    "surname",
                    "email",
                    "birth_date",
                    "birth_place",
                    "citizenship",
                    "fiscal_code",
                    "residence_address",
                ],
                # "classes": ["collapse"]
            },
        ),
        (
            _("Documenti"),
            {
                "fields": ["id_card_front", "id_card_back"],
                # "classes": ["collapse"]
            },
        ),
    ]


class CadastralDataInline(admin.StackedInline):
    model = CadastralData
    extra = 1


class CadastralDataAdmin(admin.ModelAdmin):
    list_display = [
        "property",
        "income",
        "category",
        "subcategory",
        "particle",
        "subparticle",
        "zone",
        "quarter",
        "area",
        "volume",
        "coordinates",
    ]
    search_fields = ["property"]


class PropertyAdmin(admin.ModelAdmin):
    inlines = [CadastralDataInline]
    list_display = [
        "name",
        "street",
        "city",
        "country",
    ]
    search_fields = [
        "name",
        "street",
        "city",
        "country",
    ]
    actions = ["edit_in_smoobu"]

    list_filter = ["city", "country"]
    readonly_fields = [
        "smoobu_id",
        "name",
        "street",
        "zip",
        "city",
        "country",
        "latitude",
        "longitude",
        "time_zone",
    ]

    def edit_in_smoobu(self, request, queryset):
        links = []
        for obj in queryset:
            if hasattr(obj, "smoobu_edit_link") and obj.smoobu_edit_link:
                links.append(
                    f'<a href="{obj.smoobu_edit_link}" target="_blank">{obj.name}</a>'
                )
            else:
                self.message_user(
                    request,
                    f"{obj} does not have a valid Smoobu edit link.",
                )

        if links:
            # Use `mark_safe` to allow HTML in the message
            self.message_user(
                request,
                mark_safe(f"Edit links: {' | '.join(links)}"),
            )

    edit_in_smoobu.short_description = "Edit selected items in Smoobu"


admin.site.register(Host, HostAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(CadastralData, CadastralDataAdmin)
