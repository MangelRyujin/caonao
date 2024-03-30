from django.shortcuts import render
from apps.acueducto.models import WaterPlanning

# vista para acueducto
def waterPlanning_view(request):
    water = WaterPlanning.objects.filter(active = True).order_by('in_date','in_time')
    return render(request,'waterPlanning_view.html',context={'waters':water})