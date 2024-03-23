from django.db import models
from utils.validates.validates import validate_address, validate_letters_numbers_and_spaces
from django.core.validators import MinLengthValidator
from apps.abstract.models import  ServiceWeekBase
# Create your models here.

# TypeServicePoblation model
class TypeServicePoblation(models.Model):
    """docstring for TypeServicePoblation."""
    name = models.CharField('Nombre',validators=[MinLengthValidator(3),validate_letters_numbers_and_spaces], max_length=255, blank=False , null=False, unique=True)
    
 
    class Meta:
        verbose_name= 'Tipo de servicios'
        verbose_name_plural= 'Tipos de servicios'
        
    def __str__(self) -> str:
        return self.name
    
# ServicePoblation model
class ServicePoblation(ServiceWeekBase):
    """docstring for ServicePoblation."""
    address = models.CharField('Dirección', max_length=255, validators=[MinLengthValidator(3),validate_address], blank=False , null=False)
    type_service = models.ForeignKey(TypeServicePoblation, on_delete = models.CASCADE , verbose_name='Tipo de servicio')
    
    
    class Meta:
        verbose_name= 'Institución de servicio'
        verbose_name_plural= 'Instituciones de servicios'
        
    def __str__(self) -> str:
        return f'{self.name}'
    
