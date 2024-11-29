# Generated by Django 5.1.3 on 2024-11-28 23:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0009_alter_property_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="cadastral_data",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="management.cadastraldata",
            ),
        ),
    ]
