from django.db import models
from apps.abstract.models import Base, ServiceWeekBase


# Create your models here.

# Office model
class Office(Base):
    """docstring for Office."""
    image = models.ImageField('Imagen',upload_to='consultorio/',null=True,blank=True)
 
    class Meta:
        verbose_name= 'Oficoda'
        verbose_name_plural= 'Oficodas'
        
    def __str__(self) -> str:
        return self.name
    
# ServiceOffice model
class ServiceOffice(ServiceWeekBase):
    """docstring for ServiceOffice."""
    office = models.ForeignKey(Office, on_delete = models.CASCADE , verbose_name='Oficoda')
    
    
    class Meta:
        verbose_name= 'Servicio de oficoda'
        verbose_name_plural= 'Servicios de oficoda'
        
    def __str__(self) -> str:
        return f'Servicio {self.name} de oficoda {self.office}'
    
