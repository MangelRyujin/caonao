from django.shortcuts import render

# Service view
def service_view(request):
    return render(request,'service_view.html')