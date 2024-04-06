from django.shortcuts import render
from apps.joven_club.models import JCService

def joven_club_service_view(request):
    services = JCService.objects.all()

    context = {
        'services':services
    }
    return render(request,'joven_club_view.html',context)


