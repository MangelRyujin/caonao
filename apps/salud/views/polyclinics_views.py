from django.shortcuts import render
from apps.salud.models import Polyclinics,ServicePolyclinics


def polyclinics_view(request):
    polyclinics = Polyclinics.objects.filter(active = True)

    context = {
        'polyclinics': polyclinics,
     }
    return render(request,'polyclinics_list_view.html',context)

def polyclinics_detail_view(request,pk):
    polyclinics = Polyclinics.objects.filter(
        pk = pk,
        active = True
    ).first()

    services = ServicePolyclinics.objects.filter(
         polyclinics = polyclinics,
         active = True
    )
    context = {
    'polyclinics': polyclinics,
    'services': services,
    }

    return render(request,'polyclinics_detail_view.html',context)