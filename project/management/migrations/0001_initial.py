# Generated by Django 5.1.3 on 2024-12-07 14:17

import django.db.models.deletion
import management.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Property",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "smoobu_id",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="id smoobu"
                    ),
                ),
                (
                    "booking_id",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="id booking"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="nome"
                    ),
                ),
                (
                    "street",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="via"
                    ),
                ),
                (
                    "zip",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="cap"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="città"
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="paese"
                    ),
                ),
                (
                    "latitude",
                    models.FloatField(blank=True, null=True, verbose_name="latitudine"),
                ),
                (
                    "longitude",
                    models.FloatField(
                        blank=True, null=True, verbose_name="longitudine"
                    ),
                ),
                (
                    "time_zone",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="fuso orario"
                    ),
                ),
            ],
            options={
                "verbose_name": "Proprietà",
                "verbose_name_plural": "Proprietà",
            },
        ),
        migrations.CreateModel(
            name="Channel",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="CadastralData",
            fields=[
                (
                    "property",
                    models.OneToOneField(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="management.property",
                    ),
                ),
                (
                    "section",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="sezione"
                    ),
                ),
                (
                    "sheet",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="foglio"
                    ),
                ),
                (
                    "particle",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="particella"
                    ),
                ),
                (
                    "subparticle",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="subalterno"
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="categoria"
                    ),
                ),
                (
                    "cadastrial_class",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="classe"
                    ),
                ),
                (
                    "consistency",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="consistenza"
                    ),
                ),
                (
                    "surface",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        verbose_name="superficie catastale",
                    ),
                ),
                (
                    "rent",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="rendita"
                    ),
                ),
                (
                    "code_regional",
                    models.CharField(
                        blank=True,
                        help_text="Codice identificativo regionale",
                        max_length=20,
                        null=True,
                        verbose_name="CIR",
                    ),
                ),
                (
                    "code_national",
                    models.CharField(
                        blank=True,
                        help_text="Codice identificativo nazionale",
                        max_length=20,
                        null=True,
                        verbose_name="CIN",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=management.models.property_cadastral_documents_upload_directory,
                        verbose_name="visura",
                    ),
                ),
            ],
            options={
                "verbose_name": "Dati Catastali",
                "verbose_name_plural": "Dati Catastali",
            },
        ),
        migrations.CreateModel(
            name="Host",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Nome"
                    ),
                ),
                (
                    "surname",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Cognome"
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Data di nascita"
                    ),
                ),
                ("birth_place", models.CharField(blank=True, max_length=50, null=True)),
                ("citizenship", models.CharField(blank=True, max_length=50, null=True)),
                ("fiscal_code", models.CharField(blank=True, max_length=16, null=True)),
                (
                    "residence_address",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "id_card_front",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=management.models.host_id_card_upload_directory,
                    ),
                ),
                (
                    "id_card_back",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=management.models.host_id_card_upload_directory,
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "property",
                    models.ManyToManyField(blank=True, to="management.property"),
                ),
            ],
            options={
                "verbose_name": "Host",
                "verbose_name_plural": "Hosts",
            },
        ),
        migrations.CreateModel(
            name="Reservation",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                (
                    "reference_id",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("type", models.CharField(default="reservation", max_length=50)),
                ("arrival", models.DateField()),
                ("departure", models.DateField()),
                ("created_at", models.DateTimeField()),
                ("modified_at", models.DateTimeField()),
                ("guest_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
                ("adults", models.PositiveIntegerField()),
                ("children", models.PositiveIntegerField()),
                ("check_in", models.TimeField()),
                ("check_out", models.TimeField()),
                ("notice", models.TextField(blank=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("price_paid", models.BooleanField()),
                (
                    "prepayment",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("prepayment_paid", models.BooleanField()),
                (
                    "deposit",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("deposit_paid", models.BooleanField()),
                ("language", models.CharField(default="en", max_length=5)),
                ("guest_app_url", models.URLField()),
                ("is_blocked_booking", models.BooleanField(default=False)),
                ("guest_id", models.BigIntegerField()),
                (
                    "apartment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reservations",
                        to="management.property",
                    ),
                ),
                (
                    "channel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reservations",
                        to="management.channel",
                    ),
                ),
            ],
        ),
    ]
