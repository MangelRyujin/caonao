# Generated by Django 5.0.2 on 2024-03-21 10:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("salud", "0007_serviceconsultingroom_servicepolyclinics"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="serviceconsultingroom",
            name="in_date",
        ),
        migrations.RemoveField(
            model_name="serviceconsultingroom",
            name="out_date",
        ),
        migrations.RemoveField(
            model_name="servicepolyclinics",
            name="in_date",
        ),
        migrations.RemoveField(
            model_name="servicepolyclinics",
            name="out_date",
        ),
        migrations.AddField(
            model_name="serviceconsultingroom",
            name="end_day_of_week",
            field=models.CharField(
                choices=[
                    (0, "Domingo"),
                    (1, "Lunes"),
                    (2, "Martes"),
                    (3, "Miércoles"),
                    (4, "Jueves"),
                    (5, "Viernes"),
                    (6, "Sábado"),
                ],
                default=6,
                help_text="Selecciona el dia de la semana.",
                max_length=1,
                verbose_name="Dia final del servicio",
            ),
        ),
        migrations.AddField(
            model_name="serviceconsultingroom",
            name="init_day_of_week",
            field=models.CharField(
                choices=[
                    (0, "Domingo"),
                    (1, "Lunes"),
                    (2, "Martes"),
                    (3, "Miércoles"),
                    (4, "Jueves"),
                    (5, "Viernes"),
                    (6, "Sábado"),
                ],
                default=0,
                help_text="Selecciona el dia de la semana.",
                max_length=1,
                verbose_name="Dia inicial del servicio",
            ),
        ),
        migrations.AddField(
            model_name="servicepolyclinics",
            name="end_day_of_week",
            field=models.CharField(
                choices=[
                    (0, "Domingo"),
                    (1, "Lunes"),
                    (2, "Martes"),
                    (3, "Miércoles"),
                    (4, "Jueves"),
                    (5, "Viernes"),
                    (6, "Sábado"),
                ],
                default=6,
                help_text="Selecciona el dia de la semana.",
                max_length=1,
                verbose_name="Dia final del servicio",
            ),
        ),
        migrations.AddField(
            model_name="servicepolyclinics",
            name="init_day_of_week",
            field=models.CharField(
                choices=[
                    (0, "Domingo"),
                    (1, "Lunes"),
                    (2, "Martes"),
                    (3, "Miércoles"),
                    (4, "Jueves"),
                    (5, "Viernes"),
                    (6, "Sábado"),
                ],
                default=0,
                help_text="Selecciona el dia de la semana.",
                max_length=1,
                verbose_name="Dia inicial del servicio",
            ),
        ),
    ]
