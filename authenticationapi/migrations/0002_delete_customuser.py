# Generated by Django 5.1.5 on 2025-01-15 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authenticationapi", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]
