from django.shortcuts import render
from apps.educacion.models import EducationInstitution, EducationProject


# List all education institutions
def education_list_view(request):
    education_institutions= EducationInstitution.objects.filter(active=True)
    return render(request,'education_list_view.html',education_institutions)


# List the pk education institution with all its active projects
def education_detail_view(request,pk):
    education_institution= EducationInstitution.objects.filter(
        pk=pk,
        active=True
        ).first()
    projects = EducationProject.objects.filter(
        education=pk,
        active=True
    )
    context = {'education':education_institution, 'projects':projects}
    return render(request,'education_detail_view.html',context)