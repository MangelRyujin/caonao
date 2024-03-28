from django.shortcuts import render
from apps.institucion.models import Institution,Product


# vista para las instituciones
def quiosco_view(request):
    quiosco_list = Institution.objects.filter(active = True)

    context = {
        'casilla_list': quiosco_list,
    }
    return render(request,'quiosco_list_view.html',context)

def quiosco_detail_view(request,pk):
    quiosco_institution = Institution.objects.filter(
        pk = pk,
        active = True
    ).first()
    
    products = Product.objects.filter(
        institution = pk,
        active = True
    )

    context = {
        'quiosco_institution':quiosco_institution,
        'products': products,
    }

    return render(request,'quiosco_detail_view.html',context)