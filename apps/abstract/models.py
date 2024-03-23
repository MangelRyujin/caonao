from django.db import models
from utils.validates.validates import validate_digits,validate_letters_numbers_and_spaces,validate_address
from django.core.validators import MinLengthValidator


# Create your models here.

# Base abstract model
class Base(models.Model):
    name = models.CharField('Nombre',validators=[MinLengthValidator(3),validate_letters_numbers_and_spaces], max_length=255, blank=False , null=False, unique=True)
    description = models.TextField('Descripción',validators=[MinLengthValidator(3),validate_letters_numbers_and_spaces],max_length=255, blank=False , null=False)
    address = models.CharField('Dirección', max_length=255, validators=[MinLengthValidator(3),validate_address], blank=False , null=False)
    phone = models.CharField('Teléfono',validators=[MinLengthValidator(3),validate_digits],max_length=10, blank=True , null=True )
    active = models.BooleanField('Activo', default=True)
    
    
    """docstring for Base."""
    class Meta:
        abstract = True
        
# Date, Time y Active abstract model
class DTA(models.Model):
    in_date = models.DateField('Fecha inicial',null= False, blank=False)
    in_time = models.TimeField('Hora inicial',null= False, blank=False)
    out_date = models.DateField('Fecha final',null= False, blank=False)
    out_time = models.TimeField('Hora final',null= False, blank=False)
    active = models.BooleanField('Activo', default=True)
    
    
    """docstring for DTA."""
    class Meta:
        abstract = True
        
# ServiceWeekBase abstract model
class WeekBase(models.Model):
    DAYS_OF_WEEK = (
        (0, 'Domingo'),
        (1, 'Lunes'),
        (2, 'Martes'),
        (3, 'Miércoles'),
        (4, 'Jueves'),
        (5, 'Viernes'),
        (6, 'Sábado'),
    )
    in_time = models.TimeField('Hora inicial',null= False, blank=False)
    out_time = models.TimeField('Hora final',null= False, blank=False)
    init_day_of_week = models.CharField(
        'Dia inicial del servicio',
        max_length=1,
        default=0,
        choices=DAYS_OF_WEEK,
        help_text="Selecciona el dia de la semana."
    )
    end_day_of_week = models.CharField(
        'Dia final del servicio',
        max_length=1,
        default=6,
        choices=DAYS_OF_WEEK,
        help_text="Selecciona el dia de la semana."
    )
    
    """docstring for WeekBase."""
    class Meta:
        abstract = True
        
# ServiceWeekBase abstract model
class ServiceWeekBase(models.Model):
    DAYS_OF_WEEK = (
        (0, 'Domingo'),
        (1, 'Lunes'),
        (2, 'Martes'),
        (3, 'Miércoles'),
        (4, 'Jueves'),
        (5, 'Viernes'),
        (6, 'Sábado'),
    )
    
    name = models.CharField('Nombre',validators=[MinLengthValidator(3),validate_letters_numbers_and_spaces], max_length=255, blank=False , null=False, unique=True)
    description = models.TextField('Descripción',validators=[MinLengthValidator(3),validate_letters_numbers_and_spaces],max_length=255, blank=False , null=False)
    in_time = models.TimeField('Hora inicial',null= False, blank=False)
    out_time = models.TimeField('Hora final',null= False, blank=False)
    active = models.BooleanField('Activo', default=True)
    init_day_of_week = models.CharField(
        'Dia inicial del servicio',
        max_length=1,
        default=0,
        choices=DAYS_OF_WEEK,
        help_text="Selecciona el dia de la semana."
    )
    end_day_of_week = models.CharField(
        'Dia final del servicio',
        max_length=1,
        default=6,
        choices=DAYS_OF_WEEK,
        help_text="Selecciona el dia de la semana."
    )
    
    """docstring for ServiceWeekBase."""
    class Meta:
        abstract = True