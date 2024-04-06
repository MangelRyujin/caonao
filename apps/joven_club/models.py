from django.db import models
from apps.abstract.models import  ServiceWeekBase
# Create your models here.

class JCService(ServiceWeekBase):
    cost = models.DecimalField('Costo', max_digits=10,  decimal_places=2, blank= False, null= False)

    def __str__(self) -> str:
        return f'{self.name}'