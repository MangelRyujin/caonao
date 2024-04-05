from django.db import models
from apps.abstract.models import Base,  ServiceWeekBase


# Create your models here.

# ConsultingRoom model
class ConsultingRoom(Base):
    """docstring for ConsultingRoom."""
    image = models.ImageField('Imagen',upload_to='consultorio/',null=True,blank=True)
 
    class Meta:
        verbose_name= 'Consultorio'
        verbose_name_plural= 'Consultorios'
        
    def __str__(self) -> str:
        return self.name
    
# ServiceConsultingRoom model
class ServiceConsultingRoom(ServiceWeekBase):
    """docstring for ServiceConsultingRoom."""
    consulting_room = models.ForeignKey(ConsultingRoom, on_delete = models.CASCADE , verbose_name='Consultorio')
    
    
    class Meta:
        verbose_name= 'Servicio de consultorio'
        verbose_name_plural= 'Servicios de consultorios'
        
    def __str__(self) -> str:
        return f'Servicio {self.name} consultorio {self.consulting_room}'
    

    
# Pharmacy model
class Pharmacy(Base):
    """docstring for Pharmacy."""
    image = models.ImageField('Imagen', upload_to='farmacia/',null=True,blank=True)
    
    class Meta:
        verbose_name= 'Farmacia'
        verbose_name_plural= 'Farmacias'
        
    def __str__(self) -> str:
        return self.name
    
    

    
# Polyclinics model
class Polyclinics(Base):
    """docstring for Polyclinics."""
    image = models.ImageField('Imagen', upload_to='policlinico/',null=True,blank=True)
    
    class Meta:
        verbose_name= 'Policlinico'
        verbose_name_plural= 'Policlinicos'
        
    def __str__(self) -> str:
        return self.name
    
# ServicePolyclinics model
class ServicePolyclinics(ServiceWeekBase):
    """docstring for ServicePolyclinics."""
    polyclinics = models.ForeignKey(Polyclinics, on_delete = models.CASCADE , verbose_name='Policlinico')
    
    
    class Meta:
        verbose_name= 'Servicio de policlínico'
        verbose_name_plural= 'Servicios de policlínicos'
        
    def __str__(self) -> str:
        return f'Servicio {self.name} policlínico {self.polyclinics}'
    



# SalePharmacy model
class SalePharmacy(models.Model):
    """docstring for SalePharmacy."""
    DAYS_OF_WEEK = (
        ('Domingo', 'Domingo'),
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
    )
    
    day_of_week = models.CharField(
        'Dia de venta',
        max_length=10,
        default='Domingo',
        choices=DAYS_OF_WEEK,
        help_text="Selecciona el dia de la semana."
    )
    pharmacy = models.ForeignKey(Pharmacy, on_delete = models.CASCADE , verbose_name='Farmacia')
    consulting_room = models.ForeignKey(ConsultingRoom, on_delete = models.CASCADE , verbose_name='Consultorio')
    
    class Meta:
        verbose_name= 'Venta de medicamentos'
        verbose_name_plural= 'Ventas de medicamentos'
        
    def __str__(self) -> str:
        return f'Venta el {self.day_of_week} por la farmacia {self.pharmacy} al consultorio {self.consulting_room}'
    
