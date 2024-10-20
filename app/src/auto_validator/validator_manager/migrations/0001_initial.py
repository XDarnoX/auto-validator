# Generated by Django 4.2.16 on 2024-10-20 22:44

import django.db.models.deletion
from django.db import migrations, models

import auto_validator.validator_manager.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

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
                        validators=[auto_validator.validator_manager.models.validate_hotkey_length],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subnet",
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
                ("codename", models.CharField(max_length=255, unique=True)),
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
                    models.ManyToManyField(
                        blank=True,
                        related_name="validator_list",
                        to="validator_manager.subnet",
                    ),
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
                        to="validator_manager.externalhotkey",
                    ),
                ),
                (
                    "validator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="validatorhotkey_set",
                        to="validator_manager.validator",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="externalhotkey",
            name="subnet",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="external_hotkeys",
                to="validator_manager.subnet",
            ),
        ),
        migrations.AddConstraint(
            model_name="validatorhotkey",
            constraint=models.UniqueConstraint(
                condition=models.Q(("is_default", True)),
                fields=("validator",),
                name="validator_manager_unique_default_hotkey_per_validator",
            ),
        ),
        migrations.AddConstraint(
            model_name="validatorhotkey",
            constraint=models.UniqueConstraint(
                fields=("external_hotkey",),
                name="validator_manager_unique_external_hotkey_assignment",
            ),
        ),
    ]