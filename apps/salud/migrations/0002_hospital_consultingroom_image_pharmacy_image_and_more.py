# Generated by Django 5.0.2 on 2024-03-21 04:52

import django.core.validators
import utils.validates.validates
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("salud", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hospital",
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
                    "description",
                    models.TextField(
                        max_length=255,
                        validators=[
                            django.core.validators.MinLengthValidator(3),
                            utils.validates.validates.validate_letters_numbers_and_spaces,
                        ],
                        verbose_name="Descripción",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        max_length=255,
                        validators=[
                            django.core.validators.MinLengthValidator(3),
                            utils.validates.validates.validate_address,
                        ],
                        verbose_name="Dirección",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        validators=[
                            django.core.validators.MinLengthValidator(3),
                            utils.validates.validates.validate_digits,
                        ],
                        verbose_name="Teléfono",
                    ),
                ),
                ("active", models.BooleanField(default=True, verbose_name="Activo")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="hospital/",
                        verbose_name="Imagen",
                    ),
                ),
            ],
            options={
                "verbose_name": "Hospital",
                "verbose_name_plural": "Hospitales",
            },
        ),
        migrations.AddField(
            model_name="consultingroom",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="consultorio/", verbose_name="Imagen"
            ),
        ),
        migrations.AddField(
            model_name="pharmacy",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="farmacia/", verbose_name="Imagen"
            ),
        ),
        migrations.AddField(
            model_name="polyclinics",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="policlinico/", verbose_name="Imagen"
            ),
        ),
        migrations.AlterField(
            model_name="consultingroom",
            name="name",
            field=models.CharField(
                max_length=255,
                unique=True,
                validators=[
                    django.core.validators.MinLengthValidator(3),
                    utils.validates.validates.validate_letters_numbers_and_spaces,
                ],
                verbose_name="Nombre",
            ),
        ),
        migrations.AlterField(
            model_name="consultingroom",
            name="phone",
            field=models.CharField(
                blank=True,
                max_length=10,
                null=True,
                validators=[
                    django.core.validators.MinLengthValidator(3),
                    utils.validates.validates.validate_digits,
                ],
                verbose_name="Teléfono",
            ),
        ),
        migrations.AlterField(
            model_name="pharmacy",
            name="name",
            field=models.CharField(
                max_length=255,
                unique=True,
                validators=[
                    django.core.validators.MinLengthValidator(3),
                    utils.validates.validates.validate_letters_numbers_and_spaces,
                ],
                verbose_name="Nombre",
            ),
        ),
        migrations.AlterField(
            model_name="pharmacy",
            name="phone",
            field=models.CharField(
                blank=True,
                max_length=10,
                null=True,
                validators=[
                    django.core.validators.MinLengthValidator(3),
                    utils.validates.validates.validate_digits,
                ],
                verbose_name="Teléfono",
            ),
        ),
        migrations.AlterField(
            model_name="polyclinics",
            name="name",
            field=models.CharField(
                max_length=255,
                unique=True,
                validators=[
                    django.core.validators.MinLengthValidator(3),
                    utils.validates.validates.validate_letters_numbers_and_spaces,
                ],
                verbose_name="Nombre",
            ),
        ),
        migrations.AlterField(
            model_name="polyclinics",
            name="phone",
            field=models.CharField(
                blank=True,
                max_length=10,
                null=True,
                validators=[
                    django.core.validators.MinLengthValidator(3),
                    utils.validates.validates.validate_digits,
                ],
                verbose_name="Teléfono",
            ),
        ),
    ]
