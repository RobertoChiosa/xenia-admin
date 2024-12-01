#  Copyright © Roberto Chiosa 2024.
#  Email: roberto@xeniapm.it
#  Last edited: 2/12/2024

# Third party imports
from django.contrib import admin
from django.utils.translation import gettext as _

from .models import CadastralData, Citizenship, Host, Property


class CitizenshipInline(admin.StackedInline):
    model = Citizenship
    extra = 1


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
    list_display = ["name", "address"]
    inlines = [CadastralDataInline]

    fieldsets = [
        (
            _("Anagrafica"),
            {
                "fields": [
                    "name",
                    "description",
                    "address",
                    "city",
                    "state",
                    "zipcode",
                ],
                # "classes": ["collapse"]
            },
        ),
        (
            _("APE"),
            {
                "fields": [
                    "energy_performance_certificate",
                ],
                # "classes": ["collapse"]
            },
        ),
    ]


class CitizenshipAdmin(admin.ModelAdmin):
    list_display = ["name", "code"]
    search_fields = ["name", "code"]


admin.site.register(Host, HostAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(CadastralData, CadastralDataAdmin)
admin.site.register(Citizenship, CitizenshipAdmin)
