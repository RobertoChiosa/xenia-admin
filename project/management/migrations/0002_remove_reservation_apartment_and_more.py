# Generated by Django 5.1.3 on 2024-12-07 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reservation",
            name="apartment",
        ),
        migrations.AddField(
            model_name="reservation",
            name="property_smoobu_id",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="adults",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="arrival",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="check_in",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="check_out",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="children",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="created_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="departure",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="deposit",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="deposit_paid",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="guest_app_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="guest_id",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="guest_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="is_blocked_booking",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="language",
            field=models.CharField(blank=True, default="en", max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="modified_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="notice",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="phone",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="prepayment",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="prepayment_paid",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="price_paid",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="type",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
