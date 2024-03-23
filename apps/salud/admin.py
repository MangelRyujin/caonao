from django.contrib import admin

from apps.salud.models import ConsultingRoom, Pharmacy, Polyclinics, SalePharmacy, ServiceConsultingRoom, ServicePolyclinics

# Register your models here.

@admin.register(Polyclinics)
class PolyclinicsAdmin(admin.ModelAdmin):
    list_display = ['name', 'address','phone' ,'active']
    search_fields = ['name', 'address', 'phone']

@admin.register(ServicePolyclinics)
class ServicePolyclinicsAdmin(admin.ModelAdmin):
    list_display = ['name','polyclinics' ,'active']
    search_fields = ['name']


@admin.register(ConsultingRoom)
class ConsultingRoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'address','phone' ,'active']
    search_fields = ['name', 'address', 'phone']
    
@admin.register(ServiceConsultingRoom)
class ServiceConsultingRoomAdmin(admin.ModelAdmin):
    list_display = ['name','consulting_room' ,'active']
    search_fields = ['name']
    

@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = ['name', 'address','phone' ,'active']
    search_fields = ['name', 'address', 'phone']
 

@admin.register(SalePharmacy)
class SalePharmacyAdmin(admin.ModelAdmin):
    list_display = ['pharmacy', 'consulting_room','day_of_week' ]
       
    
