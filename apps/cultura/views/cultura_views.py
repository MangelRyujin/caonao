from django.shortcuts import render

# vista para cultura
def cultura_view(request):
    return render(request,'cultura_view.html')