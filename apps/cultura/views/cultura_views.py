from django.shortcuts import render
from apps.cultura.models import CultureInstitution, CultureProject


# List all cultural institutions
def cultura_list_view(request):
    culture_institutions= CultureInstitution.objects.filter(active=True)
    return render(request,'cultura_list_view.html',culture_institutions)


# List the pk cultural institution with all its active projects
def cultura_detail_view(request,pk):
    culture_institution= CultureInstitution.objects.filter(
        pk=pk,
        active=True
        ).first()
    projects = CultureProject.objects.filter(
        culture=pk,
        active=True
    )
    context = {'culture':culture_institution, 'projects':projects}
    return render(request,'cultura_detail_view.html',context)