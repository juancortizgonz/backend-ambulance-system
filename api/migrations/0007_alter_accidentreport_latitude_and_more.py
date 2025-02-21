# Generated by Django 5.1.4 on 2025-02-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_accidentreport_severity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accidentreport",
            name="latitude",
            field=models.DecimalField(decimal_places=20, max_digits=24),
        ),
        migrations.AlterField(
            model_name="accidentreport",
            name="longitude",
            field=models.DecimalField(decimal_places=20, max_digits=24),
        ),
        migrations.AlterField(
            model_name="ambulance",
            name="latitude",
            field=models.DecimalField(decimal_places=20, max_digits=24),
        ),
        migrations.AlterField(
            model_name="ambulance",
            name="longitude",
            field=models.DecimalField(decimal_places=20, max_digits=24),
        ),
    ]
