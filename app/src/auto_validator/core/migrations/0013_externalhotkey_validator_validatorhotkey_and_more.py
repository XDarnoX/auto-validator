# Generated by Django 4.2.16 on 2024-10-24 23:02

import django.db.models.deletion
from django.db import migrations, models

import auto_validator.core.models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0012_rename_hw_requirements_subnet_hardware_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExternalHotkey",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "hotkey",
                    models.CharField(
                        max_length=48,
                        unique=True,
                        validators=[auto_validator.core.models.validate_hotkey_length],
                    ),
                ),
                ("delegate_stake_percentage", models.FloatField(default=0.0)),
                (
                    "subnet",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="external_hotkeys",
                        to="core.subnet",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Validator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("short_name", models.CharField(max_length=255, unique=True)),
                ("long_name", models.CharField(max_length=255, unique=True)),
                ("last_stake", models.IntegerField()),
                (
                    "subnets",
                    models.ManyToManyField(blank=True, related_name="validator_list", to="core.subnet"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ValidatorHotkey",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_default", models.BooleanField()),
                (
                    "external_hotkey",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="validatorhotkey",
                        to="core.externalhotkey",
                    ),
                ),
                (
                    "validator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="validatorhotkey_set",
                        to="core.validator",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="validatorhotkey",
            constraint=models.UniqueConstraint(
                condition=models.Q(("is_default", True)),
                fields=("validator",),
                name="unique_default_hotkey_per_validator",
            ),
        ),
        migrations.AddConstraint(
            model_name="validatorhotkey",
            constraint=models.UniqueConstraint(fields=("external_hotkey",), name="unique_external_hotkey_assignment"),
        ),
    ]