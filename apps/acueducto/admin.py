from django.contrib import admin
from apps.acueducto.models import WaterPlanning

# Register your models here.

@admin.register(WaterPlanning)
class BlockAdmin(admin.ModelAdmin):
    list_display = ['id','in_date','in_time', 'out_date','out_time' ,'active']
    