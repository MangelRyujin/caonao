from django.shortcuts import render
from apps.institucion.models import (Category, Institution, InstitutionService, Product,
    TypeInstitution)

# Institution list view
def institution_view(request):
    institutions_type = TypeInstitution.objects.all()

    context = {
        'institutions_type': institutions_type,
    }
    return render(request,'institution_list_view.html',context)

# Institution type view
def institutions_type_view(request,type):
    type_institution = TypeInstitution.objects.filter(
        name = type,
    ).first()
    institutions = Institution.objects.filter(
        type_institution = type_institution,
        active = True
    )
    
    
    context = {
        'institutions':institutions,
        'type':type,
    }

    return render(request,'institution_type_view.html',context)


# Institution detail for id view
def institutions_detail_view(request,pk):
    institution = Institution.objects.filter(
        pk = pk,
        active = True
    ).first()
    
    categories = Category.objects.all()
    services = InstitutionService.objects.filter(
        institution = institution,
        active = True
    )
    list_products=[]
    for category in categories:
       list_products.append({
           'category': category.name,
           'products': Product.objects.filter(
                            institution = institution,
                            active = True,
                            category=category,
                        )
       })
    context = {
        'institution':institution,
        'list_products': list_products,
        'services':services,
    }

    return render(request,'institution_detail_view.html',context)
