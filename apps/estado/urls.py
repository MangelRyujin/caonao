from django.urls import path
from apps.estado.views.estado_views import estado_view


urlpatterns = [
    path('estado',estado_view,name='estado_view'),
]