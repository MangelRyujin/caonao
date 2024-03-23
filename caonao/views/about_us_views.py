from django.shortcuts import render

# vista para el sobre nosotros
def about_us_view(request):
    return render(request,'about_us_view.html')