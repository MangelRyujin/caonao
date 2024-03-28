from django.shortcuts import render
from apps.institucion.models import Institution,Product


# vista para las instituciones
def casilla_view(request):
    casilla_list = Institution.objects.filter(active = True)

    context = {
        'casilla_list': casilla_list,
    }
    return render(request,'casilla_list_view.html',context)

def casilla_detail_view(request,pk):
    casilla_institution = Institution.objects.filter(
        pk = pk,
        active = True
    ).first()
    
    products = Product.objects.filter(
        institution = pk,
        active = True
    )

    context = {
        'bodega_institution':casilla_institution,
        'products': products,
    }

    return render(request,'casilla_detail_view.html',context)
