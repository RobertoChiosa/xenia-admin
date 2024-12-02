# Generated by Django 5.1.3 on 2024-11-28 23:27

# Third party imports
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0011_remove_cadastraldata_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="host",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="host",
            name="name",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="name"
            ),
        ),
        migrations.AlterField(
            model_name="host",
            name="property",
            field=models.ManyToManyField(blank=True, to="management.property"),
        ),
        migrations.AlterField(
            model_name="host",
            name="surname",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="surname"
            ),
        ),
    ]
