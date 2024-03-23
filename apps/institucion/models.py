from django.db import models
from utils.validates.validates import validate_address, validate_letters_numbers_and_spaces
from django.core.validators import MinLengthValidator
from apps.abstract.models import Base, ServiceWeekBase, WeekBase

# Create your models here.

# TypeServicePoblation model
class TypeInstitution(models.Model):
    """docstring for TypeInstitution."""
    name = models.CharField('Nombre',validators=[MinLengthValidator(3),validate_letters_numbers_and_spaces], max_length=255, blank=False , null=False, unique=True)
    
 
    class Meta:
        verbose_name= 'Tipo de institución'
        verbose_name_plural= 'Tipos de instituciones'
        
    def __str__(self) -> str:
        return self.name
    
# Institution model
class Institution(Base,WeekBase):
    """docstring for Institution."""
    image = models.ImageField('Imagen',upload_to='institucion/',null=False,blank=False)
    type_institution = models.ForeignKey(TypeInstitution, on_delete = models.CASCADE , verbose_name='Tipo de institución')
    
    
    class Meta:
        verbose_name= 'Institución'
        verbose_name_plural= 'Instituciones'
        
    def __str__(self) -> str:
        return f'{self.name}'

# TypeService model   
class TypeService(models.Model):
    """docstring for TypeService."""
    name = models.CharField('Nombre',validators=[MinLengthValidator(3),validate_letters_numbers_and_spaces], max_length=255, blank=False , null=False, unique=True)
    
 
    class Meta:
        verbose_name= 'Tipo de servicios'
        verbose_name_plural= 'Tipos de servicios'
        
    def __str__(self) -> str:
        return self.name
    
# InstitutionService model
class InstitutionService(ServiceWeekBase):
    """docstring for InstitutionService."""
    type_service = models.ForeignKey(TypeService, on_delete = models.CASCADE , verbose_name='Tipo de servicio')
    institution = models.ForeignKey(Institution, on_delete = models.CASCADE , verbose_name='Institución')
    
    
    class Meta:
        verbose_name= 'Servicio de institución'
        verbose_name_plural= 'Servicios de instituciones'
        
    def __str__(self) -> str:
        return f'{self.name}'
    
    
# Category model   
class Category(models.Model):
    """docstring for Category."""
    name = models.CharField('Nombre',validators=[MinLengthValidator(3),validate_letters_numbers_and_spaces], max_length=255, blank=False , null=False, unique=True)
    
 
    class Meta:
        verbose_name= 'Categoría de producto'
        verbose_name_plural= 'Categorías de productos'
        
    def __str__(self) -> str:
        return self.name
    
# Product model
class Product(models.Model):
    """docstring for Product."""
    name = models.CharField('Nombre',validators=[MinLengthValidator(3),validate_letters_numbers_and_spaces], max_length=255, blank=False , null=False, unique=True)
    cost = models.DecimalField('Costo', max_digits=10,  decimal_places=2, blank= False, null= False)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE , verbose_name='Categoría')
    
    
    class Meta:
        verbose_name= 'Producto'
        verbose_name_plural= 'Productos'
        
    def __str__(self) -> str:
        return f'{self.name}'
    


    
