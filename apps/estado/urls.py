from django.urls import path
from apps.estado.views.poblation_services_views import estado_view


urlpatterns = [
    path('estado',estado_view,name='estado_view'),
]