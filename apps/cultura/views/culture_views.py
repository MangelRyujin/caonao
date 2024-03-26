from django.shortcuts import render
from apps.cultura.models import CultureInstitution, CultureProject


# List all cultural institutions
def culture_list_view(request):
    culture_list= CultureInstitution.objects.filter(active=True)
    context = {
        'culture_list': culture_list,
    }
    return render(request,'culture_list_view.html',context)


# List the pk cultural institution with all its active projects
def culture_detail_view(request,pk):
    culture_institution= CultureInstitution.objects.filter(
        pk=pk,
        active=True
        ).first()
    projects = CultureProject.objects.filter(
        culture=pk,
        active=True
    )
    context = {'culture':culture_institution, 'projects':projects}
    return render(request,'culture_detail_view.html',context)