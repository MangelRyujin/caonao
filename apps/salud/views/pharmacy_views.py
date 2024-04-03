from django.shortcuts import render
from apps.salud.models import Pharmacy,SalePharmacy

def pharmacy_view(request):
    pharmacy = Pharmacy.objects.filter(active = True)

    context = {
        'pharmacy': pharmacy,
    }

    return render(request,'pharmacy_view.html',context)

def pharmacy_detail_view(request,pk):
    pharmacy = Pharmacy.objects.filter(
        pk = pk,
        active = True
    ).first()

    salepharmacy = SalePharmacy.objects.filter(
        pharmacy = pharmacy,
        active = True
    )

    context = {
        'pharmacy': pharmacy,
        'salepharmacy': salepharmacy,
    }

    return render(request,'pharmacy_detail_view.html',context)