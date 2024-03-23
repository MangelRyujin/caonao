from django.shortcuts import render

# vista para estado
def estado_view(request):
    return render(request,'estado_view.html')