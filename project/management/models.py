# Create your models here.


from django.db import models
from django.utils.translation import gettext_lazy as _


def host_id_card_upload_directory(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<model_name>/<id>/<filename>
    return f"{instance.__class__.__name__}/{instance.id}/id_card/{filename}"


def property_documents_upload_directory(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<model_name>/<id>/<filename>
    return f"{instance.__class__.__name__}/{instance.id}/documents/{filename}"


class Property(models.Model):
    name = models.CharField(_("name"), max_length=100, null=True, blank=True)
    description = models.TextField(_("description"), null=True, blank=True)
    address = models.CharField(_("address"), max_length=100, null=True, blank=True)
    city = models.CharField(_("city"), max_length=50, null=True, blank=True)
    state = models.CharField(_("state"), max_length=50, null=True, blank=True)
    zipcode = models.CharField(_("zipcode"), max_length=10, null=True, blank=True)
    energy_performance_certificate = models.FileField(
        verbose_name=_("APE"),
        upload_to=property_documents_upload_directory,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name or "Unnamed Property"

    class Meta:
        verbose_name = _("Proprietà")
        verbose_name_plural = _("Proprietà")


class CadastralData(models.Model):
    property = models.OneToOneField(
        to=Property, on_delete=models.CASCADE, primary_key=True, default=None
    )
    income = models.DecimalField(
        max_digits=10, decimal_places=2, default=-1, null=True, blank=True
    )
    category = models.CharField(max_length=10, null=True, blank=True)
    subcategory = models.CharField(max_length=10, null=True, blank=True)
    particle = models.CharField(max_length=10, null=True, blank=True)
    subparticle = models.CharField(max_length=10, null=True, blank=True)
    zone = models.CharField(max_length=10, null=True, blank=True)
    quarter = models.CharField(max_length=10, null=True, blank=True)
    area = models.DecimalField(
        max_digits=10, decimal_places=2, default=-1, null=True, blank=True
    )
    volume = models.DecimalField(
        max_digits=10, decimal_places=2, default=-1, null=True, blank=True
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
        return self.name

    class Meta:
        verbose_name = "host"
        verbose_name_plural = "hosts"


class Citizenship(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    code = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "cittadinanza"
        verbose_name_plural = "cittadinanze"
