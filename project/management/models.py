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
    smoobu_id = models.IntegerField(_("id smoobu"), null=True, blank=True)
    booking_id = models.IntegerField(_("id booking"), null=True, blank=True)
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
    property = models.ManyToManyField(Property, blank=True)

    def __str__(self):
        return self.name or "Senza Nome"

    class Meta:
        verbose_name = _("Host")
        verbose_name_plural = _("Hosts")
