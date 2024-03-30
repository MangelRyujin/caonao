from django.urls import path
from apps.estado.views.poblation_services_views import poblations_services_view


urlpatterns = [
    path('estado',poblations_services_view,name='poblations_services_view'),
]