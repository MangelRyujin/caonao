from django.shortcuts import render
from apps.oficoda.models import Office,ServiceOffice

# vista para la oficoda
def oficoda_view(request):
    oficoda_office = Office.objects.filter(
        active = True
        )
    context = {
        'oficoda_office':oficoda_office
    }
    return render(request,'oficoda_list.html',context)

def oficoda_service_detail_view(request,pk):
    oficoda_service = Office.objects.filter(
        pk = pk,
        active = True
    ).first()

    services = ServiceOffice.objects.filter(
        office = pk,
        active = True
    )

    context = {
        'oficoda_service':oficoda_service,
        'services':services
    }

    return render(request,'oficoda_service_detail_view.html',context)