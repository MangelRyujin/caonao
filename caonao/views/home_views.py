from django.shortcuts import render

# vista para el home
def home_view(request):
    return render(request,'home_view.html')