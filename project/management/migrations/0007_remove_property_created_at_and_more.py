# Generated by Django 5.1.3 on 2024-12-18 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0006_remove_host_property_property_host"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="property",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="property",
            name="updated_at",
        ),
    ]