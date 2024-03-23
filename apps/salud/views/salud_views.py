from django.shortcuts import render


# vista para salud
def salud_view(request):
    return render(request,'salud_view.html')