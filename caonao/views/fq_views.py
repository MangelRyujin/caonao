from django.shortcuts import render

# vista para preguntas frecuentes
def fq_view(request):
    return render(request,'fq_view.html')