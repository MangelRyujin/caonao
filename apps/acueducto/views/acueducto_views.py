from django.shortcuts import render
from apps.acueducto.models import WaterPlanning

# vista para acueducto
def acueducto_view(request):
    water = WaterPlanning.objects.filter(active = True)
    return render(request,'acueducto_view.html',water)