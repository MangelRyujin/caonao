from django.shortcuts import render
from apps.acueducto.models import WaterPlanning

# vista para acueducto
def waterPlanning_view(request):
    water = WaterPlanning.objects.filter(active = True)
    return render(request,'waterPlanning_view.html',water)