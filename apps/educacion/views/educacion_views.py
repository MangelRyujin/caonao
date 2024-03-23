from django.shortcuts import render

# vista para educacion
def educacion_view(request):
    return render(request,'educacion_view.html')