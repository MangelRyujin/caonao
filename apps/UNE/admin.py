from django.contrib import admin
from apps.UNE.models import Block, Circuit, Affectation

# Register your models here.

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ['name','active']
    search_fields = ['name']
    

@admin.register(Circuit)
class CircuitAdmin(admin.ModelAdmin):
    list_display = ['name','block','active']
    search_fields = ['name']
    
    
@admin.register(Affectation)
class AffectationAdmin(admin.ModelAdmin):
    list_display = ['block','in_date','in_time', 'out_date','out_time' ,'active']
    search_fields = ['name']
     

