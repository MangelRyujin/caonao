from django.contrib import admin

from apps.cultura.models import CultureInstitution, CultureProject

# Register your models here.


@admin.register(CultureInstitution)
class CultureInstitutionAdmin(admin.ModelAdmin):
    list_display = ['name', 'address','phone' ,'active']
    search_fields = ['name', 'address', 'phone']
    

@admin.register(CultureProject)
class CultureProjectAdmin(admin.ModelAdmin):
    list_display = ['name','culture','active']
    search_fields = ['name']
    