from django.shortcuts import render
from apps.estado.models import ServicePoblation, TypeServicePoblation

# Poblations Services view
def poblations_services_view(request):
    types = TypeServicePoblation.objects.all()
    poblations_services = []
    for type_service in types:
       poblations_services.append({
           'type': type_service.name,
           'services': ServicePoblation.objects.filter(active=True,type_service=type_service)
       })
    return render(request,'poblations_services_view.html',context={'poblations_services':poblations_services})