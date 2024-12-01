# Generated by Django 5.1.3 on 2024-11-27 17:39

# Third party imports
import management.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0006_alter_host_birth_date_alter_host_birth_place_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="host",
            name="id_card_back",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=management.models.host_id_card_upload_directory,
            ),
        ),
        migrations.AlterField(
            model_name="host",
            name="id_card_front",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=management.models.host_id_card_upload_directory,
            ),
        ),
    ]
