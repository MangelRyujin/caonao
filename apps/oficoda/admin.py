from django.contrib import admin

from apps.oficoda.models import Office, ServiceOffice

# Register your models here.
@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ['name', 'address','phone' ,'active']
    search_fields = ['name', 'address', 'phone']
    
@admin.register(ServiceOffice)
class ServiceOfficeAdmin(admin.ModelAdmin):
    list_display = ['name', 'office','active']
    search_fields = ['name']
    