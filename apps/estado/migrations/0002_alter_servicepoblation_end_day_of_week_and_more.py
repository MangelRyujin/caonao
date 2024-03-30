# Generated by Django 5.0.2 on 2024-03-30 01:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("estado", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicepoblation",
            name="end_day_of_week",
            field=models.IntegerField(
                choices=[
                    ("Domingo", "Domingo"),
                    ("Lunes", "Lunes"),
                    ("Martes", "Martes"),
                    ("Miércoles", "Miércoles"),
                    ("Jueves", "Jueves"),
                    ("Viernes", "Viernes"),
                    ("Sábado", "Sábado"),
                ],
                default=6,
                help_text="Selecciona el dia de la semana.",
                verbose_name="Dia final del servicio",
            ),
        ),
        migrations.AlterField(
            model_name="servicepoblation",
            name="init_day_of_week",
            field=models.IntegerField(
                choices=[
                    ("Domingo", "Domingo"),
                    ("Lunes", "Lunes"),
                    ("Martes", "Martes"),
                    ("Miércoles", "Miércoles"),
                    ("Jueves", "Jueves"),
                    ("Viernes", "Viernes"),
                    ("Sábado", "Sábado"),
                ],
                default=0,
                help_text="Selecciona el dia de la semana.",
                verbose_name="Dia inicial del servicio",
            ),
        ),
    ]
