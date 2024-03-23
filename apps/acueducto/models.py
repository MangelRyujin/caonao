from django.db import models
from apps.abstract.models import DTA

# Create your models here.


# WaterPlanning model
class WaterPlanning(DTA):
    """docstring for WaterPlanning."""
    
    class Meta:
        verbose_name= 'Planificación de acueducto'
        verbose_name_plural= 'Planificaciones de acueductos'
        
    def __str__(self) -> str:
        return f'Planificación {self.pk}'
