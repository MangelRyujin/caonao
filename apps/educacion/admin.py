from django.contrib import admin
from apps.educacion.models import EducationInstitution, EducationProject

# Register your models here.


@admin.register(EducationInstitution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['name', 'address','phone' ,'active']
    search_fields = ['name', 'address', 'phone']
    

@admin.register(EducationProject)
class EducationProjectAdmin(admin.ModelAdmin):
    list_display = ['name','education','active']
    search_fields = ['name']
    