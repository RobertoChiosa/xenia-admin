from django.db import models

# Create your models here.

from django.db import models
from django.utils.translation import gettext as _
from datetime import datetime


def host_id_card_upload_directory(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<model_name>/<id>/<filename>
    return f'{instance.__class__.__name__}/{instance.id}/id_card/{filename}'


class Property(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "properties"


class Host(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default=None)
    surname = models.CharField(max_length=50, default=None)
    birth_date = models.DateField( default=None)
    birth_place = models.CharField(
        max_length=50, default=None
    )
    citizenship = models.CharField(
        max_length=50, default=None
    )
    fiscal_code = models.CharField(
        max_length=16, default=None
    )
    residence_address = models.CharField(
        max_length=100, default=None
    )
    residence_city = models.CharField(
        max_length=50, default=None
    )
    residence_zipcode = models.CharField(
        max_length=10, default=None
    )
    residence_state = models.CharField(
         max_length=50, default=None
    )
    id_card_front = models.FileField(upload_to=host_id_card_upload_directory, default=None)
    id_card_back = models.FileField(upload_to=host_id_card_upload_directory, default=None)
    email = models.EmailField(default=None)
    property = models.ManyToManyField(Property)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "hosts"
