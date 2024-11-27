from django.db import models

# Create your models here.

from django.db import models
from django.utils.translation import gettext as _
from datetime import datetime


def host_id_card_upload_directory(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<model_name>/<id>/<filename>
    return f'{instance.__class__.__name__}/{instance.id}/id_card/{filename}'

def property_documents_upload_directory(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<model_name>/<id>/<filename>
    return f'{instance.__class__.__name__}/{instance.id}/documents/{filename}'


from django.db import models
from django.utils.translation import gettext_lazy as _


class Property(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    cadastral_income = models.DecimalField(max_digits=10, decimal_places=2, default=-1, null=True, blank=True)
    cadastral_category = models.CharField(max_length=10, null=True, blank=True)
    cadastral_subcategory = models.CharField(max_length=10, null=True, blank=True)
    cadastral_particle = models.CharField(max_length=10, null=True, blank=True)
    cadastral_subparticle = models.CharField(max_length=10, null=True, blank=True)
    cadastral_zone = models.CharField(max_length=10, null=True, blank=True)
    cadastral_quarter = models.CharField(max_length=10, null=True, blank=True)
    cadastral_area = models.DecimalField(max_digits=10, decimal_places=2, default=-1, null=True, blank=True)
    cadastral_volume = models.DecimalField(max_digits=10, decimal_places=2, default=-1, null=True, blank=True)
    cadastral_coordinates = models.CharField(max_length=50, null=True, blank=True)
    cadastral_map = models.FileField(
        verbose_name=_("Mappa catastale"),
        upload_to=property_documents_upload_directory,
        null=True,
        blank=True
    )
    cadastral_sheet = models.FileField(
        verbose_name=_("Visura catastale"),
        upload_to=property_documents_upload_directory,
        null=True,
        blank=True
    )
    energy_performance_certificate = models.FileField(
        verbose_name=_("APE"),
        upload_to=property_documents_upload_directory,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name or "Unnamed Property"

    class Meta:
        verbose_name_plural = "properties"


class Host(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True,null=True)
    surname = models.CharField(max_length=50, blank=True,null=True)
    birth_date = models.DateField(null=True, blank=True)
    birth_place = models.CharField(
        max_length=50, null=True, blank=True)
    citizenship = models.CharField(
        max_length=50, null=True, blank=True)
    fiscal_code = models.CharField(
        max_length=16, null=True, blank=True)
    residence_address = models.CharField(
        max_length=100, null=True, blank=True)
    residence_city = models.CharField(
        max_length=50, null=True, blank=True)
    residence_zipcode = models.CharField(
        max_length=10, null=True, blank=True)
    residence_state = models.CharField(
         max_length=50, null=True, blank=True)
    id_card_front = models.FileField(upload_to=host_id_card_upload_directory, null=True, blank=True)
    id_card_back = models.FileField(upload_to=host_id_card_upload_directory, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    property = models.ManyToManyField(Property, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "hosts"
