from django.db import models
from apps.abstract.models import DTA
from utils.validates.validates import validate_letters_numbers_and_spaces
from django.core.validators import MinLengthValidator

# Create your models here.


# Block model
class Block(models.Model):
    """docstring for Block."""
    name = models.CharField('Nombre',validators=[MinLengthValidator(1),validate_letters_numbers_and_spaces], max_length=255, blank=False , null=False, unique=True)
    active = models.BooleanField('Activo', default=True)
    
    class Meta:
        verbose_name= 'Bloque'
        verbose_name_plural= 'Bloques'
        
    def __str__(self) -> str:
        return self.name

# Circuit model
class Circuit(models.Model):
    """docstring for Circuit."""
    name = models.CharField('Nombre',validators=[MinLengthValidator(3),validate_letters_numbers_and_spaces], max_length=255, blank=False , null=False, unique=True)
    block = models.ForeignKey(Block, on_delete=models.CASCADE,verbose_name='Bloque', null=True, blank=True)
    active = models.BooleanField('Activo', default=True)
    
    class Meta:
        verbose_name= 'Circuito'
        verbose_name_plural= 'Circuitos'
        
    def __str__(self) -> str:
        return self.name
    
# Affectation model
class Affectation(DTA):
    """docstring for Affectation."""
    block = models.ForeignKey(Block, on_delete=models.CASCADE,verbose_name='Bloque', null=False, blank=False)
    
    class Meta:
        verbose_name= 'Afectación'
        verbose_name_plural= 'Afectaciones'
        
    def __str__(self) -> str:
        return f'Afectación en el bloque {self.block}'
