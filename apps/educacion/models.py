from django.db import models
from apps.abstract.models import Base
from utils.validates.validates import validate_letters_numbers_and_spaces
from django.core.validators import MinLengthValidator

# Create your models here.


# Institution model
class EducationInstitution(Base):
    """docstring for Institution."""
    image = models.ImageField('Imagen',upload_to='institution_education/',null=False,blank=False)
 
    
    class Meta:
        verbose_name= 'Institución de educación'
        verbose_name_plural= 'Instituciones de educación'
        
    def __str__(self) -> str:
        return self.name
    
# EducationProject model
class EducationProject(models.Model):
    """docstring for EducationProject."""
    name = models.CharField('Nombre',validators=[MinLengthValidator(1),validate_letters_numbers_and_spaces], max_length=255, blank=False , null=False, unique=True)
    description = models.TextField('Descripción',validators=[MinLengthValidator(3),validate_letters_numbers_and_spaces],max_length=255, blank=True , null=True)
    active = models.BooleanField('Activo', default=True)
    education = models.ForeignKey(EducationInstitution, on_delete= models.CASCADE,verbose_name='Institución')
    
    class Meta:
        verbose_name= 'Proyecto de educación'
        verbose_name_plural= 'Proyectos de educación'
        
    def __str__(self) -> str:
        return self.name
    
