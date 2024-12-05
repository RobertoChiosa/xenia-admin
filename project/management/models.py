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


def property_documents_upload_directory(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<model_name>/<id>/<filename>
    return f"{instance.__class__.__name__}/{instance.id}/documents/{filename}"


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
    smoobu_id = models.IntegerField(_("smoobu_id"), null=True, blank=True)
    name = models.CharField(_("name"), max_length=100, null=True, blank=True)
    street = models.CharField(_("street"), max_length=100, null=True, blank=True)
    zip = models.CharField(_("zip"), max_length=10, null=True, blank=True)
    city = models.CharField(_("city"), max_length=50, null=True, blank=True)
    country = models.CharField(_("country"), max_length=50, null=True, blank=True)
    latitude = models.CharField(_("latitude"), max_length=50, null=True, blank=True)
    longitude = models.CharField(_("longitude"), max_length=50, null=True, blank=True)
    time_zone = models.CharField(_("time_zone"), max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name or "Senza Nome"

    class Meta:
        verbose_name = _("Proprietà")
        verbose_name_plural = _("Proprietà")


class CadastralData(models.Model):
    property = models.OneToOneField(
        to=Property, on_delete=models.CASCADE, primary_key=True, default=None
    )
    income = models.DecimalField(
        max_digits=10, decimal_places=2, default=None, null=True, blank=True
    )
    category = models.CharField(max_length=10, null=True, blank=True)
    subcategory = models.CharField(max_length=10, null=True, blank=True)
    particle = models.CharField(max_length=10, null=True, blank=True)
    subparticle = models.CharField(max_length=10, null=True, blank=True)
    zone = models.CharField(max_length=10, null=True, blank=True)
    quarter = models.CharField(max_length=10, null=True, blank=True)
    area = models.DecimalField(
        max_digits=10, decimal_places=2, default=None, null=True, blank=True
    )
    volume = models.DecimalField(
        max_digits=10, decimal_places=2, default=None, null=True, blank=True
    )
    coordinates = models.CharField(max_length=50, null=True, blank=True)
    map = models.FileField(
        verbose_name=_("Mappa catastale"),
        upload_to=property_documents_upload_directory,
        null=True,
        blank=True,
    )
    sheet = models.FileField(
        verbose_name=_("Visura catastale"),
        upload_to=property_documents_upload_directory,
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
