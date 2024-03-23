from django.db import models
from apps.abstract.models import DTA, Base
from utils.validates.validates import validate_letters_numbers_and_spaces
from django.core.validators import MinLengthValidator

# Create your models here.


# Institution model
class CultureInstitution(Base):
    """docstring for Institution."""
    image = models.ImageField('Imagen',upload_to='institution_education/',null=False,blank=False)
 
    
    class Meta:
        verbose_name= 'Institución de cultura'
        verbose_name_plural= 'Instituciones de cultura'
        
    def __str__(self) -> str:
        return self.name
    
# EducationProject model
class CultureProject(DTA):
    """docstring for EducationProject."""
    name = models.CharField('Nombre',validators=[MinLengthValidator(1),validate_letters_numbers_and_spaces], max_length=255, blank=False , null=False, unique=True)
    description = models.TextField('Descripción',validators=[MinLengthValidator(3),validate_letters_numbers_and_spaces],max_length=255, blank=True , null=True)
    culture = models.ForeignKey(CultureInstitution, on_delete= models.CASCADE,verbose_name='Institución')
    
    
    class Meta:
        verbose_name= 'Proyecto de cultura'
        verbose_name_plural= 'Proyectos de cultura'
        
    def __str__(self) -> str:
        return self.name
    
