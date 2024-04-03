from django.shortcuts import render
from apps.salud.models import ConsultingRoom,ServiceConsultingRoom


def consultingroom_view(request):
    consultingroom = ConsultingRoom.objects.filter(active = True)

    context = {
        'consultingroom': consultingroom,
     }
    return render(request,'consultingroom_list_view.html',context)

def consultingroom_detail_view(request,pk):
    consultingroom = ConsultingRoom.objects.filter(
        pk = pk,
        active = True
    ).first()

    services = ServiceConsultingRoom.objects.filter(
         consultingroom = consultingroom,
         active = True
    )
    context = {
    'consultingroom': consultingroom,
    'services': services,
    }

    return render(request,'consultingroom_detail_view.html',context)
