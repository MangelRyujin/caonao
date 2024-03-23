# Generated by Django 5.0.2 on 2024-03-21 06:17

import django.core.validators
import django.db.models.deletion
import utils.validates.validates
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Block",
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
                (
                    "name",
                    models.CharField(
                        max_length=255,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(3),
                            utils.validates.validates.validate_letters_numbers_and_spaces,
                        ],
                        verbose_name="Nombre",
                    ),
                ),
            ],
            options={
                "verbose_name": "Bloque",
                "verbose_name_plural": "Bloques",
            },
        ),
        migrations.CreateModel(
            name="Affectation",
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
                ("in_date", models.DateField(verbose_name="Fecha inicial")),
                ("in_time", models.TimeField(verbose_name="Hora inicial")),
                ("out_date", models.DateField(verbose_name="Fecha final")),
                ("out_time", models.TimeField(verbose_name="Hora final")),
                ("active", models.BooleanField(default=True, verbose_name="Activo")),
                (
                    "block",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UNE.block",
                        verbose_name="Bloque",
                    ),
                ),
            ],
            options={
                "verbose_name": "Bloque",
                "verbose_name_plural": "Bloques",
            },
        ),
        migrations.CreateModel(
            name="Circuit",
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
                (
                    "name",
                    models.CharField(
                        max_length=255,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(3),
                            utils.validates.validates.validate_letters_numbers_and_spaces,
                        ],
                        verbose_name="Nombre",
                    ),
                ),
                (
                    "block",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UNE.block",
                        verbose_name="Bloque",
                    ),
                ),
            ],
            options={
                "verbose_name": "Cicuito",
                "verbose_name_plural": "Cicuitos",
            },
        ),
    ]
