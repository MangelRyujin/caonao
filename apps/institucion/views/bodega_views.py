from django.shortcuts import render
from apps.institucion.models import Institution,Product


# vista para las instituciones
def bodega_view(request):
    bodega_list = Institution.objects.filter(active = True,)

    context = {
        'bodega_list': bodega_list,
    }
    return render(request,'institution_list_view.html',context)

def bodega_detail_view(request,pk):
    bodega_institution = Institution.objects.filter(
        pk = pk,
        active = True
    ).first()
    
    products = Product.objects.filter(
        institution = pk,
        active = True
    )

    context = {
        'bodega_institution':bodega_institution,
        'products': products,
    }

    return render(request,'institution_detail_view.html',context)
