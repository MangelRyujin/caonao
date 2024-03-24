from django.shortcuts import render

# vista para las instituciones
def institucion_view(request):
    return render(request,'instutucion_view.html')