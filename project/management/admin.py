from django.contrib import admin

from .models import Host, Property
from django.utils.translation import gettext as _

class HostAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "surname", "email"]

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
                ],
                # "classes": ["collapse"]
            },
        ),
        (
            _("Residenza"),
            {
                "fields": [
                    "residence_address",
                    "residence_city", "residence_zipcode" ,"residence_state",
                ],
                # "classes": ["collapse"]
            },
        ),
        (
            _("Documenti"),
            {
                "fields": [
                    "id_card_front",
                    "id_card_back"
                ],
                # "classes": ["collapse"]
            },
        ),

    ]


class PropertyAdmin(admin.ModelAdmin):
    list_display = ["name", "address"]

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
            _("Visura Catastale"),
            {
                "fields": [
                   "cadastral_income",
                   "cadastral_category",
                   "cadastral_subcategory",
                   "cadastral_particle",
                   "cadastral_subparticle",
                   "cadastral_zone",
                   "cadastral_quarter",
                   "cadastral_area",
                   "cadastral_map",
                   "cadastral_sheet",
                ],
                "classes": ["collapse"]
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


admin.site.register(Host, HostAdmin)
admin.site.register(Property, PropertyAdmin)
