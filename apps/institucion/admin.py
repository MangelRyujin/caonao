from django.contrib import admin

from apps.institucion.models import (Category, Institution, InstitutionService, Product,
    TypeInstitution, TypeService)

# Register your models here.
@admin.register(TypeInstitution)
class TypeInstitutionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['name','type_institution','phone','address','active']
    search_fields = ['name']
    
@admin.register(TypeService)
class TypeServiceAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(InstitutionService)
class InstitutionServiceAdmin(admin.ModelAdmin):
    list_display = ['name','type_service','institution','active']
    search_fields = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','cost','active']
    search_fields = ['name']

