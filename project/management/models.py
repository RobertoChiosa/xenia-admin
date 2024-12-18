#  Copyright © Roberto Chiosa 2024.
#  Email: roberto@xeniapm.it
#  Last edited: 6/12/2024

# Create your models here.


# Third party imports
from django.db import models
from django.utils.translation import gettext_lazy as _


def host_id_card_upload_directory(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<model_name>/<id>/<filename>
    return f"{instance.__class__.__name__}/{instance.id}/id_card/{filename}"


def property_cadastral_documents_upload_directory(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<model_name>/<id>/<filename>
    return f"{instance.__class__.__name__}/{instance.property_id}/visura_{filename}"


# {
#     "location": {
#         "street": "Wönnichstr. 68/70",
#         "zip": "10317",
#         "city": "Berlin",
#         "country": "Germany",
#         "latitude": "52.5200080000000",
#         "longitude": "13.4049540000000"
#     },
#    "timeZone": "Europe/Berlin",
#     "rooms": {
#         "maxOccupancy": 4,
#         "bedrooms": 4,
#         "bathrooms": 2,
#         "doubleBeds": 1,
#         "singleBeds": 3,
#         "sofaBeds": null,
#         "couches": null,
#         "childBeds": null,
#         "queenSizeBeds": null,
#         "kingSizeBeds": 1
#
#     },
#     "equipments": [
#         "Internet",
#         "Whirlpool",
#         "Pool",
#         "Heating"
#     ],
#     "currency": "EUR",
#     "price": {
#             "minimal": "10.00",
#             "maximal": "100.00"
#     },
#     "type": {
#         "id": 2,
#         "name": "Holiday rental"
#     }
# }


class Property(models.Model):
    smoobu_id = models.IntegerField(_("id smoobu"), null=True, blank=True, unique=True)
    booking_id = models.IntegerField(
        _("id booking"), null=True, blank=True, unique=True
    )
    host = models.ForeignKey(
        "Host",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="properties",
    )
    name = models.CharField(_("nome"), max_length=100, null=True, blank=True)
    street = models.CharField(_("via"), max_length=100, null=True, blank=True)
    zip = models.CharField(_("cap"), max_length=10, null=True, blank=True)
    city = models.CharField(_("città"), max_length=50, null=True, blank=True)
    country = models.CharField(_("paese"), max_length=50, null=True, blank=True)
    latitude = models.FloatField(_("latitudine"), null=True, blank=True)
    longitude = models.FloatField(_("longitudine"), null=True, blank=True)
    time_zone = models.CharField(_("fuso orario"), max_length=50, null=True, blank=True)

    @property
    def smoobu_edit_link(self):
        return f"https://login.smoobu.com/it/settings/apartments/edit/{self.smoobu_id}"

    @property
    def booking_edit_link(self):
        return f"https://admin.booking.com/hotel/hoteladmin/extranet_ng/manage/home.html?hotel_id={self.booking_id}&lang=it"

    def __str__(self):
        return self.name or "Senza Nome"

    class Meta:
        verbose_name = _("Proprietà")
        verbose_name_plural = _("Proprietà")


class CadastralData(models.Model):
    property = models.OneToOneField(
        to=Property, on_delete=models.CASCADE, primary_key=True, default=None
    )
    section = models.CharField(_("sezione"), max_length=20, null=True, blank=True)
    sheet = models.CharField(_("foglio"), max_length=20, null=True, blank=True)
    particle = models.CharField(_("particella"), max_length=20, null=True, blank=True)
    subparticle = models.CharField(
        _("subalterno"), max_length=20, null=True, blank=True
    )
    category = models.CharField(_("categoria"), max_length=20, null=True, blank=True)
    cadastrial_class = models.CharField(
        _("classe"), max_length=20, null=True, blank=True
    )
    consistency = models.CharField(
        _("consistenza"), max_length=20, null=True, blank=True
    )
    surface = models.CharField(
        _("superficie catastale"), max_length=20, null=True, blank=True
    )
    rent = models.CharField(_("rendita"), max_length=20, null=True, blank=True)
    code_regional = models.CharField(
        _("CIR"),
        help_text="Codice identificativo regionale",
        max_length=20,
        null=True,
        blank=True,
    )
    code_national = models.CharField(
        _("CIN"),
        help_text="Codice identificativo nazionale",
        max_length=20,
        null=True,
        blank=True,
    )
    file = models.FileField(
        _("visura"),
        upload_to=property_cadastral_documents_upload_directory,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.property.name or "Senza Nome"

    class Meta:
        verbose_name = _("Dati Catastali")
        verbose_name_plural = _("Dati Catastali")


class Host(models.Model):
    name = models.CharField(_("Nome"), max_length=50, blank=True, null=True)
    surname = models.CharField(_("Cognome"), max_length=50, blank=True, null=True)
    birth_date = models.DateField(_("Data di nascita"), null=True, blank=True)
    birth_place = models.CharField(max_length=50, null=True, blank=True)
    citizenship = models.CharField(max_length=50, null=True, blank=True)
    fiscal_code = models.CharField(max_length=16, null=True, blank=True)
    residence_address = models.CharField(max_length=100, null=True, blank=True)
    id_card_front = models.FileField(
        upload_to=host_id_card_upload_directory, null=True, blank=True
    )
    id_card_back = models.FileField(
        upload_to=host_id_card_upload_directory, null=True, blank=True
    )
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = _("Host")
        verbose_name_plural = _("Hosts")


class Channel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    reference_id = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(_("tipo"), max_length=50, null=True, blank=True)
    arrival = models.CharField(_("arrivo"), max_length=255, null=True, blank=True)
    departure = models.CharField(_("partenza"), max_length=255, null=True, blank=True)
    created_at = models.CharField(_("creato il"), max_length=255, null=True, blank=True)
    modified_at = models.CharField(
        _("modificato il"), max_length=255, null=True, blank=True
    )
    property = models.ForeignKey(
        Property, to_field="smoobu_id", on_delete=models.CASCADE, null=True, blank=True
    )
    channel = models.CharField(_("canale"), max_length=255, null=True, blank=True)
    guest_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    adults = models.PositiveIntegerField(null=True, blank=True)
    children = models.PositiveIntegerField(null=True, blank=True)
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    notice = models.TextField(
        blank=True,
        null=True,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_paid = models.CharField(max_length=50, null=True, blank=True)
    prepayment = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True, blank=True
    )
    prepayment_paid = models.CharField(max_length=50, null=True, blank=True)
    deposit = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True, blank=True
    )
    deposit_paid = models.CharField(max_length=50, null=True, blank=True)
    language = models.CharField(max_length=5, default="en", null=True, blank=True)
    guest_app_url = models.URLField(null=True, blank=True)
    is_blocked_booking = models.CharField(
        max_length=50, default=False, null=True, blank=True
    )
    guest_id = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Prenotazione {self.id} da {self.guest_name}"

    class Meta:
        verbose_name = _("Prenotazione")
        verbose_name_plural = _("Prenotazioni")
