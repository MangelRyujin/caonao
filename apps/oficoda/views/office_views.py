from django.shortcuts import render


# vista para la oficoda
def oficoda_view(request):
    return render(request,'oficoda_view.html')