# Generated by Django 5.1.3 on 2024-12-18 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0005_property_created_at_property_updated_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="host",
            name="property",
        ),
        migrations.AddField(
            model_name="property",
            name="host",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="properties",
                to="management.host",
            ),
        ),
    ]