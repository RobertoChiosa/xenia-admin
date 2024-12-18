#  Copyright © Roberto Chiosa 2024.
#  Email: roberto@xeniapm.it
#  Last edited: 6/12/2024

# Third party imports
from django.contrib import admin
from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _
from unfold.admin import ModelAdmin, StackedInline
from unfold.decorators import display, action

from .models import CadastralData, Host, Property, Reservation


class HostInline(StackedInline):
    model = Host
    extra = 1
    tab = True
    classes = ["wide"]


class CadastralDataInline(StackedInline):
    model = CadastralData
    extra = 1
    tab = True
    classes = ["wide"]
    fieldsets = (
        (
            None,
            {
                "fields": [
                    (
                        "code_regional",
                        "code_national",
                    ),
                ]
            },
        ),
        (
            None,
            {
                "fields": [
                    (
                        "section",
                        "sheet",
                        "particle",
                        "subparticle",
                    ),
                    (
                        "category",
                        "consistency",
                        "surface",
                        "rent",
                    ),
                    "file",
                ],
            },
        ),
    )


class CadastralDataAdmin(ModelAdmin):
    list_display = [
        "property",
        "code_regional",
        "code_national",
        # "section",
        # "sheet",
        # "particle",
        # "subparticle",
        # "category",
        # "consistency",
        # "surface",
        # "rent",
        "file",
    ]
    search_fields = ["property", "code_regional", "code_national"]
    fieldsets = (
        (
            "Anagrafica",
            {
                "fields": [
                    "property",
                    (
                        "code_regional",
                        "code_national",
                    ),
                ]
            },
        ),
        (
            "Dati Catastali",
            {
                "fields": [
                    (
                        "section",
                        "sheet",
                        "particle",
                        "subparticle",
                    ),
                    (
                        "category",
                        "consistency",
                        "surface",
                        "rent",
                    ),
                    "file",
                ],
            },
        ),
    )


class PropertyInline(StackedInline):
    model = Property
    extra = 1
    tab = True
    classes = ["wide"]
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


class HostAdmin(ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "surname", "email", "fiscal_code"]
    inlines = [PropertyInline]
    fieldsets = [
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


# todo export excel
class PropertyAdmin(ModelAdmin):
    inlines = [CadastralDataInline]
    list_display = ["name", "street", "city"]

    search_fields = [
        "name",
        "street",
        "city",
    ]

    list_filter = ["city"]

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

    fieldsets = [
        (
            _("Anagrafica"),
            {
                "fields": [
                    "name",
                    (
                        "street",
                        "zip",
                        "city",
                        "country",
                    ),
                    (
                        "latitude",
                        "longitude",
                        "time_zone",
                    ),
                ],
                # "classes": ["collapse"]
            },
        ),
        (
            _("Portali"),
            {
                "fields": [
                    (
                        "booking_id",
                        "smoobu_id",
                    ),
                ],
                # "classes": ["collapse"]
            },
        ),
    ]

    @display(description=_("Booking edit"), ordering="booking_edit_link")
    def display_booking_edit_link(self, instance: Property):
        return instance.booking_edit_link

    @action(description="Modifica in Smoobu")
    def edit_in_smoobu(self, request, queryset):
        """
        Redirects to the Smoobu edit link for the selected object.
        """
        if queryset.count() > 1:
            self.message_user(
                request,
                _("You can only edit one property at a time"),
                level=messages.ERROR,
            )
            return
        property = queryset.first()
        if property.smoobu_id is None:
            self.message_user(
                request,
                _("This property is not linked to Smoobu"),
                level=messages.ERROR,
            )
            return
        return HttpResponseRedirect(property.smoobu_edit_link)

    actions_detail = ["edit_in_smoobu"]


class ReservationAdmin(ModelAdmin):
    list_display = [
        "property",
        # "id",
        # "reference_id",
        "type",
        "arrival",
        "departure",
        # "created_at",
        # "modified_at",
        "channel",
        "guest_name",
        "email",
        # "phone",
        "adults",
        "children",
        "check_in",
        "check_out",
        # "notice",
        "price",
        "price_paid",
        # "prepayment",
        # "prepayment_paid",
        # "deposit",
        # "deposit_paid",
        "language",
        # "guest_app_url",
        # "is_blocked_booking",
        # "guest_id",
    ]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "reference_id",
                    "guest_id",
                    "type",
                    "property",
                    "channel",
                )
            },
        ),
        (
            "Dettagli prenotazione",
            {"fields": ("arrival", "departure", "check_in", "check_out", "notice")},
        ),
        (
            "Informazioni Ospite",
            {
                "fields": (
                    "guest_name",
                    "email",
                    "phone",
                    "adults",
                    "children",
                    "language",
                    "guest_app_url",
                )
            },
        ),
        (
            "Prezzo",
            {
                "fields": (
                    "price",
                    "price_paid",
                    "prepayment",
                    "prepayment_paid",
                    "deposit",
                    "deposit_paid",
                )
            },
        ),
    )

    readonly_fields = [
        "id",
        "reference_id",
        "type",
        "arrival",
        "departure",
        # "property_smoobu_id",
        "channel",
        "guest_name",
        "email",
        "phone",
        "adults",
        "children",
        "check_in",
        "check_out",
        "notice",
        "price",
        "price_paid",
        "prepayment",
        "prepayment_paid",
        "deposit",
        "deposit_paid",
        "language",
        "guest_app_url",
        "is_blocked_booking",
        "guest_id",
    ]


admin.site.register(Host, HostAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(CadastralData, CadastralDataAdmin)
admin.site.register(Reservation, ReservationAdmin)
