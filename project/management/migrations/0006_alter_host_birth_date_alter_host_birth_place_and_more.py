# Generated by Django 5.1.3 on 2024-11-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "management",
            "0005_alter_property_address_alter_property_cadastral_area_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="host",
            name="birth_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="host",
            name="birth_place",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="host",
            name="citizenship",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="host",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="host",
            name="fiscal_code",
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name="host",
            name="name",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="host",
            name="property",
            field=models.ManyToManyField(
                blank=True, null=True, to="management.property"
            ),
        ),
        migrations.AlterField(
            model_name="host",
            name="residence_address",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="host",
            name="residence_city",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="host",
            name="residence_state",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="host",
            name="residence_zipcode",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="host",
            name="surname",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
