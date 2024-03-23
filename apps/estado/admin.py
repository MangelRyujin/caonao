from django.contrib import admin
from apps.estado.models import ServicePoblation, TypeServicePoblation

# Register your models here.
@admin.register(TypeServicePoblation)
class TypeServicePoblationAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    

@admin.register(ServicePoblation)
class ServicePoblationAdmin(admin.ModelAdmin):
    list_display = ['name','type_service','address','active']
    search_fields = ['name']
    