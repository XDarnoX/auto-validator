# Generated by Django 4.2.16 on 2024-09-16 14:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_rename_code_name_subnet_codename_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="subnet",
            old_name="mainnet_netid",
            new_name="mainnet_id",
        ),
        migrations.RenameField(
            model_name="subnet",
            old_name="testnet_netid",
            new_name="testnet_id",
        ),
    ]